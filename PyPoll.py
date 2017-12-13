import csv
import os

def PyPoll(inputfilepath):

    #open the input file to read from
    with open(inputfilepath, 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            next(csvreader, None)

            #Initializing/declaring the summary variables
            list_candidates = {}
            percentage_votes = 0
            candidate_vote = 0
            total_votes = 0
            
            for row in csvreader:
                total_votes = total_votes+1
                key = row[2]
                if (key not in list_candidates.keys()):
                    list_candidates[key] = 0
                candidate_vote = list_candidates[key]
                candidate_vote=candidate_vote + 1
                list_candidates[key]= candidate_vote

            for key in list_candidates.keys():
                votes = list_candidates[key]
                percentage_votes= round((100/total_votes)*list_candidates[key],2)
                list_candidates[key]=[]
                list_candidates[key].append(votes)
                list_candidates[key].append(percentage_votes)

            winner = max(list_candidates, key=list_candidates.get)


                    
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(total_votes))
    print("-------------------------")
    for key, value in list_candidates.items():
        print(key+ ": " +str(value[1])+ "%" + " ("+ str(value[0])+ ")")
    print("-------------------------")
    print("Winner: "+ winner)
    print("-------------------------")


PyPoll('resources1/election_data_1.csv')
PyPoll('resources1/election_data_2.csv')
