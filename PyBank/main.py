import os 
import csv

budget_path = "resources/budget_data.csv"
totalmonths = 0
totalnet = 0
netchangelist = []
greatestincrease = ["", 0]
greatestdecrease = ["", 999999999]

with open(budget_path, "r") as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader, None)

    firstrow = next(csv_reader)
    totalmonths += 1
    totalnet = int(firstrow[1])
    previousnet = totalnet

    for row in csv_reader:
        totalmonths += 1
        totalnet += int(row[1])
        netchange = int(row[1]) - previousnet
        previousnet = int(row[1])
        netchangelist.append(netchange)

        if netchange > greatestincrease[1]:
            greatestincrease[0] = row[0]
            greatestincrease[1] = netchange
        
        if netchange < greatestdecrease[1]:
            greatestdecrease[0] = row[0]
            greatestdecrease[1] = netchange

monthlyaverage = sum(netchangelist) / len(netchangelist)

output = (
    f" Financial Analysis\n"
  f"----------------------------\n"
  f"Total Months: {totalmonths}\n"
  f"Total: ${totalnet}\n"
  f"Average  Change: ${monthlyaverage}\n"
  f"Greatest Increase in Profits: {greatestincrease[0]} (${greatestincrease[1]})\n"
  f"Greatest Decrease in Profits: {greatestdecrease[0]} (${greatestdecrease[1]})\n"
)
print(output)
# Net Total Profit/Loss over Entire Period --


