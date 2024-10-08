# Assignment 2
# CSV file provided - Assignment to create a plot of temperature over time in a Jupyter Notebook
#
# Attempt 1 - retrieved variables from CSV and plotted them
#
# Issues 
# [1] -> The temperature variables are accurate to 15 decimal places - labelling is very messy
# [2] -> The date and time and in format 2024-10-03T12:30:00+00:00 - labelling is very messy

# Ideas:
# [1] -> display  
# [2]

import csv
import matplotlib.pyplot as plt

FILENAME = "weatherreadings1.csv"
DATADIR = "./"

x = []
y = []

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    for line in reader:
        #print(line["reportStartDateTime"],"\t",line["dryBulbTemperature_Celsius"])
        #print(type(line["dryBulbTemperature_Celsius"]))
        
        x.append(line["reportStartDateTime"])
        y.append(float(line["dryBulbTemperature_Celsius"]))
        
    fig, ax = plt.subplots()

    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
    ax.set_xlabel("Day and Date")
    ax.set_ylabel("Temperature Celsius")
    ax.set_title("Temperature Variation")
    #ax.axhline()
    
    #ax.set_xticks()
    #plt.autoscale(enable=True, axis='both', tight=None)
    plt.show()

    #print(type(y[0]))
