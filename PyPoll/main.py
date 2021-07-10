# Modules
import os
import csv

#Create dictionary
election_votes = {}
percentage_votes= {}

# Set path for file
csvpath = os.path.join("Resources","election_data.csv")

# set variables to 0
total = 0

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    # firstrow = next(csvreader)    
    for row in csvreader:
        total += 1
        if row [2] not in election_votes.keys():
            election_votes [row[2]]=1
        election_votes [row[2]]+=1

for key, value in election_votes.items():
    percentage_votes [key]= round(value/total *100,2)

for key, value in election_votes.items():
    print (f"{key}: {percentage_votes[key]}% ({value})")

# print (election_votes)
print (total)
# print (percentage_votes)
