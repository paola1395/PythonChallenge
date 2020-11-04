import os
import csv
import sys

candidates_list=[]
votes=0
Khan_votes=0
Correy_votes=0
Li_votes=0
Otooley_votes=0


csvpath= os.path.join("Resources/election_data.csv")

#Set path, open with csv.reader and skip header
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    next(csvreader)

#Loop through CSV & count votes. Determine winner.
    for row in csvreader:
        votes +=1
        if row[2] not in candidates_list:
            candidates_list.append(row[2])

        if row[2]== "Khan":
            Khan_votes +=1
        elif row[2]== "Correy":
            Correy_votes +=1
        elif row[2]== "Li":
            Li_votes +=1
        elif row[2]== "O'Tooley":
            Otooley_votes +=1
        
        if Khan_votes > Correy_votes and Khan_votes > Li_votes and Khan_votes > Otooley_votes:
            winner = "Winner: Khan"
        elif Correy_votes > Khan_votes and Correy_votes > Li_votes and Correy_votes > Otooley_votes:
            winner= "Winner: Correy"
        elif Li_votes > Khan_votes and Li_votes > Correy_votes and Li_votes > Otooley_votes:
            winner= "Winner: Li"
        elif Otooley_votes > Khan_votes and Otooley_votes > Correy_votes and Otooley_votes > Li_votes:
            winner= "Winner: O'Tooley"
        
        #Print election results

        print("Election Results")
        print("-------------------------")
        print("Candidates:", candidates_list[0] + ",", candidates_list[1] + ",", candidates_list[2] + ",", candidates_list[3])
        print("-------------------------")
        print("Total Votes:", votes)
        print("-------------------------")

        k_percent=round(((Khan_votes/votes)*100),2)
        print("Khan:", str(k_percent)+"%", "(" + str(Khan_votes)+ ")")
        c_percent=round(((Correy_votes/votes)*100),2)
        print("Correy:", str(c_percent)+"%", "(" + str(Correy_votes)+ ")")
        l_percent=round(((Li_votes/votes)*100),2)
        print("Li:", str(l_percent)+"%", "(" + str(Li_votes)+ ")")
        o_percent=round(((Otooley_votes/votes)*100),2)
        print("O'Tooley:", str(o_percent)+"%", "(" + str(Otooley_votes)+ ")")
        print("-------------------------")

        print(winner)
        print("-------------------------")

#text file
stdoutOrigin=sys.stdout 
txtPath = os.path.join("Analysis/election_analysis.txt")
sys.stdout = open(txtPath, "w")

print("Election Results")
print("-------------------------")
print("Candidates:", candidates_list[0] + ",", candidates_list[1] + ",", candidates_list[2] + ",", candidates_list[3])
print("-------------------------")
print("Total Votes:", votes)
print("-------------------------")

k_percent=round(((Khan_votes/votes)*100),2)
print("Khan:", str(k_percent)+"%", "(" + str(Khan_votes)+ ")")
c_percent=round(((Correy_votes/votes)*100),2)
print("Correy:", str(c_percent)+"%", "(" + str(Correy_votes)+ ")")
l_percent=round(((Li_votes/votes)*100),2)
print("Li:", str(l_percent)+"%", "(" + str(Li_votes)+ ")")
o_percent=round(((Otooley_votes/votes)*100),2)
print("O'Tooley:", str(o_percent)+"%", "(" + str(Otooley_votes)+ ")")
print("-------------------------")

print(winner)
print("-------------------------")

sys.stdout.close()
sys.stdout=stdoutOrigin




            



