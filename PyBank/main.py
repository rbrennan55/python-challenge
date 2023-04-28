# File Name: main.py
# Import the os module.  This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Clears the screan
os.system('cls')

# Initialize variables to hold totals

total_months = 0
total = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_pair = ['',0]
greatest_decrease_pair = ['',999999999999]
next_change_list = []
month_change_list = []

# Open and read file budget_data.csv
csvfilepath = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvfilepath) as csvinputfile:

    # CSV reader specifies delimiter and variable that holds contents
    
    csvreader = csv.reader(csvinputfile, delimiter=',')
      
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    csv_first_entry = next(csvreader)   
    total_months += 1
    total += int(csv_first_entry[1])
    previous = int(csv_first_entry[1])
    
    
    # Read each row of data after the header
    
    for row in csvreader:
        # Incremental count of the months
        total_months += 1

        # Incremental count of Profit/Loss
        total += int(row[1])
        
        change = int(row[1]) - previous
        previous = int(row[1])

        next_change_list += [change]
        month_change_list += [row[0]]
   
        # Incremental comparison of the higher Profit/loss with day
        if change > greatest_increase_pair[1]:
            greatest_increase_pair[1] = change
            greatest_increase_pair[0] = row[0]
            
        # Incremental comparison of the lower Profit/loss with day    
        if change < greatest_decrease_pair[1]:
            greatest_decrease_pair[1] = change
            greatest_decrease_pair[0] = row[0]
# Close the file
csvinputfile.close()            


# Calculate the average change
average_change = round((sum(next_change_list)/len(next_change_list)),2)


# Save to File
outputfilepath = os.path.join('.', 'analysis', 'budget_data_analysis.txt')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(outputfilepath, 'w') as outputfile:

    # Initialize csv.writer
    outputfile.write("\nFinancial Analysis\n\n")
    for dash in range(20):
      outputfile.write("-")
        
    outputfile.write("\n\nTotal Months: " + str(total_months) + "\n")
    outputfile.write("\nTotal: $" + str(total) +"\n")
    outputfile.write("\nAverage Change: $" + str(average_change) +"\n")
    outputfile.write("\nGreatest Increase in Profits: " + str(greatest_increase_pair[0]) + " ($" + str(greatest_increase_pair[1]) + ")\n")
    outputfile.write("\nGreatest Decrease in Profits: " + str(greatest_decrease_pair[0]) +  " ($" + str(greatest_decrease_pair[1]) + ")\n")
    outputfile.close()

 
# Output to screen        
print("\n\nFinancial Analysis\n")
for dash in range(20):
    print("-", end = " ")

print(f"\n\nTotal Months: {total_months}\n")
print(f"\nTotal: ${total}\n")
print(f"\nAverage Change: ${average_change}\n")
print(f"\nGreatest Increase in Profits: {greatest_increase_pair[0]} (${greatest_increase_pair[1]})\n")
print(f"\nGreatest Decrease: {greatest_decrease_pair[0]} (${greatest_decrease_pair[1]})\n")


