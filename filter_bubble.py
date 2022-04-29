import csv


IN_FILENAME = "./rawdata/2019-20_pbp.csv"
OUT_FILENAME = "./bubble-data.csv"
results = dict()    # GameID, GameData
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
            score_diff = abs(home_score - away_score)
            score_total = home_score + away_score
            game_res = {
                "HomeScore" :   home_score,
                "AwayScore" :   away_score,
                "ScoreDiff" :   score_diff,
                "ScoreTotal":   score_total
            }

            results[game_id] = game_res


with open(OUT_FILENAME, "w") as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow(
            ["GameID", "HomeScore", "AwayScore",
            "ScoreDiff", "ScoreTotal"]
    )

    for game_id, game_res in results.items():

        new_row = [game_id] + list(game_res.values())
        writer.writerow(new_row)
