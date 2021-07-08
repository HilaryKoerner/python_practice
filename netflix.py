import os
import csv

csvpath = os.path.join(".", 'Resources', 'netflix_ratings.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #print(csvreader)

    user_movie = print("What movie are you looking for?")

    print(user_movie)