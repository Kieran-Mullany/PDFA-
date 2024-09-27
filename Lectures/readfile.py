#read in a file

FILENAME = "data.txt"
DATADIR = "../PDFA/"

print(DATADIR + FILENAME)

with open(DATADIR + FILENAME, "rt") as fp:
    total = 0
    for line in fp:
        total += int(line)
        #print (line, end="")
    print(f"{line} is size {len(FILENAME)}")
    print(f"\ntotal is {total}")
