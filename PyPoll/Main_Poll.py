import os
import csv

vote_index= [0,0,0,0]
canidates_list=[]
all_votes=[]
canidates = {}


election_data= os.path.join("resources/election_data.csv")


#Set path, open with csv.reader and skip header
with open(election_data, newline="") as electioncsv:
    csvreader=csv.reader(electioncsv, delimiter=",")
    next(csvreader)

    #Variables

    votes=0

    for row in csvreader:
        votes= votes+1
        if row[2] not in canidates_list:
            canidates_list.append(row[2])
        all_votes.append(row[2])



