import os 
import csv

budget_path = "resources/budget_data.csv"

with open(budget_path, "r") as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter=",")

print("Financial Analysis" )
print("-------------------")

# Total Number of Months --
count_of_months = 0
with open(budget_path) as file:
    csv_reader_object = csv.reader(file)
    if csv.Sniffer().has_header:
        next(csv_reader_object)
    
    for row in csv_reader_object:
        count_of_months += 1

totalmonths = count_of_months
print("Total Months: " + str(totalmonths))

# Net Total Profit/Loss over Entire Period --
with open(budget_path) as file:
    if csv.Sniffer().has_header:
        next(csv_reader_object)

data = list(csv_reader)
totals1 = [] 
for row in data:
     values = row[1] 
     totals1.append(values)          
     totals2 = [float(integral) for integral in totals1] #turns values in totals1 into floats
     totals3 = sum(totals2) 

print(totals3)