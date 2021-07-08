import os
import csv

user_movie = print(input("What movie are you looking for?"))

csvpath = os.path.join(".", 'Resources', 'netflix_ratings.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #print(csvreader)

    

    print(user_movie)

    