# Add our dependencies.
import csv
import os

# Assign a variable to load the input file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the output file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter BEFORE opening output file
total_votes = 0

# Decalring candidate options list
candidate_options = []

# Declaring candidate votes dictionary to hold tally: candidiate_name, votes tally
candidate_votes = {}

# Declaring a variable for Winning Candidate, Winning Count Tracker, and Winning Percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file; "with" will open, read, and close.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row test the next() function
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count; more simple syntax to total_votes = total_votes + 1
        total_votes += 1

        # Print the candidate name from each row; first iteration
        candidate_name = row[2]

        # Check the candidate_name not already in list before appending
        if candidate_name not in candidate_options:
            # If true then add new occurrance of candidate_name to list 
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count by initialling vote count to 0 as new name is found.
            candidate_votes[candidate_name] = 0
            
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.  
        #print(f"{candidate_name}: received {vote_percentage: .1f}% of the vote.")

        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
     
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    
        #  To do: print out the winning candidate, vote count and percentage to terminal.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")  

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


# Print out tests.
    #print(total_votes)
    #print(candidate_options)
    #print(candidate_votes)
