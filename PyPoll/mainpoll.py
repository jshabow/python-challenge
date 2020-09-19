import os
import csv
#Variables
election_path = "resources/election_data.csv"
totalvotes = 0
votes = []
candidates = []
uniquecandidate = []
vote_count = []
percentage = []
#Open File
with open(election_path, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)
#Total Votes
    firstrow = next(csv_reader)
    for row in csv_reader:
      totalvotes += 1
#Append candidate names for their results
      if row[2] not in uniquecandidate:
        uniquecandidate.append(row[2])

      votes.append(row[2])
#Calculate total # of votes and percentages
    for candidate in uniquecandidate:
      vote_count.append(votes.count(candidate))
      percentage.append(round(votes.count(candidate)/totalvotes*100,3))
#Find the candidate with the most votes
    winner = uniquecandidate[vote_count.index(max(vote_count))]

#formatting my output
output = (
    f"Election Results\n"
  f"-------------------------\n"
  f"Total Votes: {totalvotes}\n"
  f"-------------------------\n"
)

print(output)

for i in range(len(uniquecandidate)):
  print(f'{uniquecandidate[i]}: {percentage[i]}% ({vote_count[i]})')

output2 = ( 
  f"-------------------------\n"
  f"Winner: {winner}\n"
  f"-------------------------\n"
)
print(output2)
#creating output file ath
poll_output = 'analysis/poll_output.txt'

#printing output to txt file
with open(poll_output,'w') as txtfile:
    txtfile.write('Election Results\n')
    txtfile.write('-------------------------\n')
    txtfile.write(f'Total Votes: {totalvotes}\n')
    txtfile.write('-------------------------\n')
    for i in range (len(uniquecandidate)):
             txtfile.write(f'\n{uniquecandidate[i]}: {percentage[i]}% {vote_count[i]}\n')
    txtfile.write('-------------------------\n')
    txtfile.write(f'Winner: {winner}\n')
    txtfile.write('------------------------------------\n')
