import os 
import csv
#Variables
budget_path = "resources/budget_data.csv"
totalmonths = 0
totalnet = 0
netchangelist = []
greatestincrease = ["", 0]
greatestdecrease = ["", 999999999]
# Open File
with open(budget_path, "r") as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)
#Total Months
    firstrow = next(csv_reader)
    totalmonths += 1
    #Total profit/losses
    totalnet = int(firstrow[1])
    previousnet = totalnet
#Average Change profit/losses
    for row in csv_reader:
        totalmonths += 1
        totalnet += int(row[1])
        netchange = int(row[1]) - previousnet
        previousnet = int(row[1])
        netchangelist.append(netchange)
#Greatest Increase
        if netchange > greatestincrease[1]:
            greatestincrease[0] = row[0]
            greatestincrease[1] = netchange
#Greatest Decrease       
        if netchange < greatestdecrease[1]:
            greatestdecrease[0] = row[0]
            greatestdecrease[1] = netchange

monthlyaverage = sum(netchangelist) / len(netchangelist)

output = (
    f" Financial Analysis\n"
  f"----------------------------\n"
  f"Total Months: {totalmonths}\n"
  f"Total: ${totalnet}\n"
  f"Average  Change: ${round(monthlyaverage,2)}\n"
  f"Greatest Increase in Profits: {greatestincrease[0]} (${greatestincrease[1]})\n"
  f"Greatest Decrease in Profits: {greatestdecrease[0]} (${greatestdecrease[1]})\n"
)
print(output)

bank_output = "analysis/bank_output.txt"

with open(bank_output, 'w') as txtfile:
    txtfile.write('Financial Analysis\n')
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {totalmonths}\n")
    txtfile.write(f"Total: ${totalnet}\n")
    txtfile.write(f"Average  Change: ${round(monthlyaverage,2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatestincrease[0]} (${greatestincrease[1]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatestdecrease[0]} (${greatestdecrease[1]})\n")