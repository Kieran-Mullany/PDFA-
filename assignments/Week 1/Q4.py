# Modify the program to calculate the average age
# My Attempt

import csv

FILENAME = "data.csv"
DATADIR = "./"

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    total = 0
    for line in reader:
        if not linecount:
            print(f"{line}\n-------------------")
        else:   
            total += int(line[1])
        linecount += 1
    average = total / (linecount - 1)
    print(average)