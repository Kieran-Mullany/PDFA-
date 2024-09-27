# Modify the program to calculate the average age
# Using quote parameters

import csv

FILENAME = "data.csv"
DATADIR = "./"

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",", quoting = csv.QUOTE_NONNUMERIC)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount:
            print(f"{line}\n-------------------")
        else:   
            total += line[1]
        linecount += 1
    average = total / (linecount - 1)
    print(average)