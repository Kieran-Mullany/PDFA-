# Modify the program to calculate the average age
# My Attempt

import csv

FILENAME = "data.csv"
DATADIR = "./"

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    linecount = 0
    for line in reader:
            total += line['age']
            linecount += 1
    average = total / (linecount)
    print(average)