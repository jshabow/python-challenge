import os
import csv

election_path = "resources/election_data.csv"
totalvotes = 0

with open(election_path, "r") as csvfile:
    csv_reader = csvreader(csvfile, delimiter=",")
    next(csv_reader, None)

    firstrow = next(csv_reader)

