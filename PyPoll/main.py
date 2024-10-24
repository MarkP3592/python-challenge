# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_list = {}

# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        
        # Print a loading indicator (for large datasets)
        #print(". ", end="")
        
        # Increment the total vote count for each row
        total_votes = total_votes + 1

        # Get the candidate's name from the row
        candidate = str(row[2])
        # If the candidate is not already in the candidate list, add them
        if candidate not in candidate_list:
            candidate_list[candidate] = 0

        # Add a vote to the candidate's count
        candidate_list[candidate] += 1

    # Calculate vote percentages and winning candidate
    candidate_percentages = {}
    for candidate, votes in candidate_list.items():
        percentage = (votes / total_votes) * 100
        candidate_percentages[candidate] = percentage

    winning_candidate = max(candidate_percentages, key=candidate_percentages.get)

    # Print to terminal
    print(total_votes)
    print(candidate_list)
    print(candidate_percentages)
    print(winning_candidate)
    

# Open a text file to save the output and save the winning candidate summary to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("----------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-----------------\n")
    # loop through candidate dictionary to find and write vote percentages
    for candidate, votes in candidate_list.items():
        percentage = (votes / total_votes) * 100
        txt_file.write(f"{candidate}: {percentage:.3f} ({votes})\n")

    txt_file.write("-----------------\n")
    txt_file.write(f"Winner: {winning_candidate}\n")
    txt_file.write("-----------------\n")

