
#to call the file and assign a variable to the file
file_to_load = 'Resources/election_results.csv'

#to open and read election data file 
#election_data = open(file_to_load, 'r').

#open election results and read file using WITH
with open(file_to_load) as election_data:

#to do: Peform Analysis

#Close file - data stored once file is closed; no need if using WITH statement
#election_data.close()

    print(election_data)




#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote
