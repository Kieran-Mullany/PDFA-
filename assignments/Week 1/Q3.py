import csv

FILENAME = "data.csv"
DATADIR = "./"

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    for line in reader:
        if not linecount:
            print(f"{line}\n-------------------")
        else:   
            print(line)
        linecount += 1