import csv

FILENAME = "data.csv"
DATADIR = "./"

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    for line in reader:
        print(line,"\t",type(line))