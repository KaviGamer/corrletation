import numpy as np
import csv

def find_correlation():
    coffeeinml = []
    sleep = []
    with open("coffee.csv") as f:
        data = csv.DictReader(f)
        for row in data:
            coffeeinml.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
        datasource = {"x":sleep,"y":coffeeinml}
        correlation = np.corrcoef(datasource["x"],datasource["y"])
        print(correlation[0,1])

find_correlation()