import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    coffee_in_ml = []
    sleep_in_hours = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee_in_ml.append(float(row["Coffee in ml"]))
            sleep_in_hours.append(float(row["sleep in hours"]))
    return {"x": coffee_in_ml,"y":sleep_in_hours}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Coffee in ml and sleep in hrs is ",correlation[0,1])

def setup():
    data_path= './cups of coffee vs hours of sleep.csv'
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)

setup()