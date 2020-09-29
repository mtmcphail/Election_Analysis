# Add our dependencies.
import csv
import os

# Assign a variable to load the input file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the output file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file; with will open, read, and close.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    #for row in file_reader:
    #    print(row)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)