import os
import csv

video = input("What movie are you looking for?")

csvpath = os.path.join(".", 'Resources', 'netflix_ratings.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        if row[0] == video:
            print(row[0] + "is rated " + row[1] + "with a viewer rating of " + row[5])
        elif row[0] != video:
            print("We do not have that video")
            break
    