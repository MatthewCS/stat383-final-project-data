import csv


# sourced from https://www.basketball-reference.com/leagues/NBA_stats_per_game.html
IN_FILENAME = "./rawdata/nba_stats_per_game.csv"
OUT_FILENAME = "./points-per-game-data.csv"
results = [ ]


with open(IN_FILENAME, "r") as csvfile:

    reader = csv.DictReader(csvfile)

    for row in reader:

        if row["Season"] != "2019-20":

            points = float(row["PTS"])
            results.append([row["Season"], points])


with open(OUT_FILENAME, "w") as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow(
        ["Season", "PointsPerTeam"]
    )

    for season in results:

        writer.writerow(season)
