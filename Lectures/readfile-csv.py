#read in a file

import csv

FILENAME = "data.csv"
DATADIR = "../"

print(DATADIR + FILENAME)

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",",quoting=csv.QUOTE_ALL)
    total = 0
    linenumber = 0
    for line in reader:
        if linenumber == 0:
            print(line)
        else:
            print(line[0])
            #total += int(line[0])
            
        linenumber += 1
    
    print(f"\ntotal is {total}")
