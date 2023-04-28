# File Name:main.py
# Import the os module.  This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Clears the screan
os.system('cls')

# Function Definitions
def buildCandiateList(candidateName, numvotes):
    # Check if candidate is in dictionary
    # if NOT add to dictionary
    # if PRESENT add to vote count - use varaiable += then update key:value  
    if candidateName not in candidate:
        candidate[candidateName] = (int(numvotes))
    else:
        previos_vote_count = candidate.get(candidateName)
        candidate[candidateName] = (int(previos_vote_count + numvotes))
    return candidate


def getWinner(candidate_results):
    # Returns the winner (key) based on get funtion of the max value 
    winner = max(candidate_results, key = candidate_results.get)
    return winner


def getVotePercent(candidate_votes, total_votes):
    # Returns the vote percentage per candidate
    percentVotes = (candidate_votes/total_votes) * 100
    # Rounds the math to 3 decimal places
    return round(percentVotes,3)

def printDashes(num):
    # Prints number of defined 'Dashes' as seperators
    for dash in range(20):
        print("-", end = " ")
    print("\n")
    return

# Initialize variables to hold values

total_votes = 0
total_votes_per_candiate = 0
candidate_results = []
candidate_winner = ""
percent_votes = 0
candidate = {}

# Open and read file budget_data.csv
csvfilepath = os.path.join('.', 'Resources', 'election_data.csv')

with open(csvfilepath) as csvinputfile:

    # CSV reader specifies delimiter and variable that holds contents
    
    csvreader = csv.reader(csvinputfile, delimiter=',')
      
    # Read the header row first 
    csv_header = next(csvreader)
    csv_first_entry = next(csvreader)   
    current_candidate_name = (csv_first_entry[2])
    total_votes = 1
                 
    # Read each row of data after the header
    
    for row in csvreader:
        # Incremental count of votes
        total_votes += 1
        
        next_candidate_name = row[2] 

        # Loop through list and count candidates
        if current_candidate_name == next_candidate_name:
            total_votes_per_candiate += 1 
            
        else:
            total_votes_per_candiate += 1
            candidate_results = buildCandiateList(current_candidate_name, total_votes_per_candiate)
            current_candidate_name = next_candidate_name
            total_votes_per_candiate = 0
            
    total_votes_per_candiate += 1
    candidate_results = buildCandiateList(current_candidate_name, total_votes_per_candiate)         
    candidate_winner = getWinner(candidate_results)

           
      
csvinputfile.close()            
# Save to File

outputfilepath = os.path.join('.', 'analysis', 'election_data_analysis.txt')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(outputfilepath, 'w') as outputfile:

    # Initialize csv.writer
    
    outputfile.write("\nElection Results\n")
    # Writes number of defined 'Dashes' as seperators
    for dash in range(25):
      outputfile.write("-")
    
    # Writes the total numnber of votes
    outputfile.write(f"\n\nTotal Votes: {total_votes}\n\n")
    
    # Writes number of defined 'Dashes' as seperators
    for dash in range(25):
      outputfile.write("-")
    outputfile.write("\n")
   
    #while loop for candiate name, percent vote and totall votes per candiate
    for key, value in candidate_results.items():
        candidate_percent = getVotePercent(value,total_votes)
        outputfile.write(f"\n{key}: {candidate_percent}% ({value})\n")
    outputfile.write("\n")
    # Wites number of defined 'Dashes' as seperators
    for dash in range(25):
      outputfile.write("-")

    # Writes the winner
    outputfile.write(f"\n\nWinner: {candidate_winner}\n\n")
    for dash in range(25):
      outputfile.write("-")
    # Closes file
    outputfile.close()

# Output to screen        
print("\nElection Results\n")

# Prints number of defined 'Dashes' as seperators
printDashes(20)

# Prints the total numnber of votes
print(f"Total Votes: {total_votes}\n")

# Prints number of defined 'Dashes' as seperators
printDashes(20)

#while loop for candiate name, percent vote and totall votes per candiate
for key, value in candidate_results.items():
    candidate_percent = getVotePercent(value,total_votes)
    print(f"\n{key}: {candidate_percent}% ({value})\n")
    #print (key,":", candidate_percent, "%", "(",value,")\n")

# Prints number of defined 'Dashes' as seperators
printDashes(20)

# Prints the winner
print(f"Winner: {candidate_winner}\n")
printDashes(20)
