import csv


IN_FILENAME = "./rawdata/2019-20_pbp.csv"
OUT_FILENAME = "./bubble-lead-changes.csv"
results = [ ]   # GameID, Year, LeadChanges
current_id = ""
current_year = "2019-20"
current_lead_changes = 0
leader = "start"  # can be start, home, away
bubble_arenas = {
        "The Arena Bay Lake Florida",
        "HP Field House Bay Lake Florida",
        "Visa Athletic Center Bay Lake Florida"
}

with open(IN_FILENAME, "r") as csvfile:

    reader = csv.DictReader(csvfile)

    for row in reader:

        if row["Location"] in bubble_arenas:

            # each URL starts with "/boxscores/"
            # ".html"
            # we strip this out of the URL for our ID
            # "/boxscores/" is 11 characters long
            # ".html" is 5 characters long
            game_id = row["URL"][11:-5]
            home_score = int(row["HomeScore"])
            away_score = int(row["AwayScore"])

            # we're on a new game
            if current_id != game_id:

                # write the old game, if not blank
                if current_id != "":

                    results.append([current_id, current_year, current_lead_changes])

                current_id = game_id
                current_lead_changes = 0
                home_leading = True

            # we're on the current game
            else:

                if leader == "start":

                    if home_score > away_score:

                        leader = "home"

                    elif away_score > home_score:

                        leader = "away"

                elif leader == "home":

                    if away_score > home_score:

                        leader = "away"
                        current_lead_changes += 1

                else:

                    if home_score > away_score:

                        leader = "home"
                        current_lead_changes += 1


with open(OUT_FILENAME, "w") as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow(
            ["GameID", "Year", "LeadChanges"]
    )

    for game in results:

        writer.writerow(game)
