# This script is where we manipulate the database

from csv import reader

# Simple way to read the file
# with open('books.csv') as database:
#     bl = database.read()
# print(bl)

# Reading using csv_reader
with open('books.csv') as database:
    bl = reader(database)
    next(bl)
    lbl = list(bl)

for line in lbl:
    print(f'Title: {line[0]}; Author: {line[1]}; Genre: {line[2]}; Height: {line[3]}; Publisher: {line[4]}')
