# File Name:main.py
# Import the os module.  This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Clears the screan
os.system('cls')

# Function Definitions
def candidate_votes(candiadate, numvotes):

# Initialize variables to hold values

total_votes = 0
total_votes_per_candiate = 0
percentage_of_votes_per_candiate = 0
candidate_results = []
candiate_winner = ""
percent_votes = 0

# Open and read file budget_data.csv
csvfilepath = os.path.join('.', 'Resources', 'election_data.csv')

with open(csvfilepath) as csvinputfile:

    # CSV reader specifies delimiter and variable that holds contents
    
    csvreader = csv.reader(csvinputfile, delimiter=',')
      
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    csv_first_entry = next(csvreader)   
    total_votes += 1
    total_votes_per_candiate += 1
    current_candidate_name = (csv_first_entry[2])
             
    # Read each row of data after the header
        
    for row in csvreader:
        # Incremental count of votes
        
        total_votes += 1
        print (current_candidate_name)
        this_candidate_name = row[2] 
        if current_candidate_name == this_candidate_name:
            total_votes_per_candiate =+ 1
            currentCandidate(this_candidate_name)
        else:
            percent_votes = total_votes_per_candiate/total_votes
            candidate_results = (current_candidate_name, percent_votes, total_votes_per_candiate)




             
    print(candidate_results)
        
        # Set profit gains and losses for comparison
        #profit_gain = int(row[1])
        #profit_loss = int(row[1])

        # Incremental comparison of the highest Profit/loss with day
        #if profit_gain > greatest_increase:
         #   greatest_increase = profit_gain
         #   greatest_increase_pair = [row[0], row[1]]
            
        # Incremental comparison of the highest Profit/loss with day    
        #if profit_loss < greatest_decrease:
         #   greatest_decrease = profit_loss
          #  greatest_decrease_pair = [row[0], row[1]]
csvinputfile.close()            
# Save to File
'''
outputfilepath = os.path.join('.', 'analysis', 'election_data_analysis.txt')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(outputfilepath, 'w') as outputfile:

    # Initialize csv.writer
    #outputwriter = writer(outputfile)

    outputfile.write("\nFinancial Analysis\n\n")
    for dash in range(20):
      outputfile.write("-")
        
    # csvwriter.writerow(seperator)

    outputfile.write("\n\nTotal Months: " + str(total_months) + "\n")
    outputfile.write("\nTotal: $" + str(total) +"\n")
    outputfile.write("\nAverage Change: $" + str(average_change) +"\n")
    outputfile.write("\nGreatest Increase in Profits: " + str(greatest_increase_pair[0]) + " ($" + str(greatest_increase_pair[1]) + ")\n")
    outputfile.write("\nGreatest Decrease in Profits: " + str(greatest_decrease_pair[0]) +  " ($" + str(greatest_decrease_pair[1]) + ")\n")
    outputfile.close()

    
'''
    
 
# Output to screen        
print("\n\nElection Results\n")
for dash in range(20):
    print("-", end = " ")

print(f"\n\nTotal Votes: {total_votes}\n")
for dash in range(20):
    print("-", end = " ")
#while loop for candiate name, percent vote and toal votes per candiate

print(f"\n{candidate_results[0]}: {candidate_results[1]}% ({candidate_results[2]})\n")

print(f"\nWinner: {candiate_winner}\n")


