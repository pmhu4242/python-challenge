import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
total_votes = 0

candidates = {}
percentage_votes={} 
candidate_votes= {}

vote_winner=0
votes = []

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader: 
        print(row)

        total_votes += 1
        i = (row[2])
        

        if i in candidate_votes:
            candidate_votes[i] += 1
        else:
            candidate_votes[i] = 1

output_path = os.path.join("Analysis", "pypoll_results.txt")
with open(output_path, 'w') as txtfile:
    
    print("Election Results", file=txtfile)
    print("Election Results")
    print('-----------------------------------', file=txtfile)
    print('-----------------------------------')
    print(f'Total Votes {total_votes}', file=txtfile)
    print(f'Total Votes {total_votes}')
    print('-----------------------------------', file=txtfile)
    print(f'----------------------------------')      
        


    for key, votes in candidate_votes.items():
        percentage_votes = round(((votes/total_votes)*100),3)
        
        print(f'{key}: {percentage_votes}% ({votes})', file=txtfile)
        print(f'{key}: {percentage_votes}% ({votes})')
        
        if votes > vote_winner:
            vote_winner = votes
            key = total_votes
            winner = i
    print('-----------------------------------', file=txtfile)
    print('-------------------------------------')
    print(f'Winner: {i}', file=txtfile)
    print(f'Winner: {i}')
    print('-----------------------------------', file=txtfile)
    print('-------------------------------------')


    