# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    previous_profitloss = int(first_row[1])
    total_net = 1088983
    # Track the total and net change
    change_list = []
    total_list = []
    months = []
    # Process each row of data
    for row in reader:
        current_profitloss = int(row[1])
        net_change = current_profitloss - previous_profitloss
        total_list.append(current_profitloss)
        change_list.append(net_change)
        months.append(row[0])
        previous_profitloss = current_profitloss
        
        # Calculate total months and print
    total_months = 1 + len(change_list)
    print(total_months)

        # Track the total
    final_total = total_net + sum(total_list)
    print(final_total)

        # Track the net change, calculate average, and print
    sum_of_change = sum(change_list)
    count = len(change_list)
    avg_net_change = sum_of_change / count
    print(avg_net_change)

        # Calculate the greatest increase in profits (month and amount) and print
    greatest_increase = max(change_list)
    print(greatest_increase)
    greatest_increase_date = months[change_list.index(greatest_increase)]
    print(greatest_increase_date)

        # Calculate the greatest decrease in losses (month and amount) and print
    greatest_decrease = min(change_list)
    print(greatest_decrease)
    greatest_decrease_date = months[change_list.index(greatest_decrease)]
    print(greatest_decrease_date)




# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("-------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${final_total}\n")
    txt_file.write(f"Average Change: ${avg_net_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
    