![vote_pic](./Resources/vote_image.jpeg)
# Election Analysis of Colorado's 1st Congressional District


## Overview of Election Audit
A Colorado Board of Elections employee, Tom, was given the tasks to complete an audit of a recent election for Colorado's 1st Congressional District. This district contains spans Denver and parts of Arapahoe and Jefferson counties.

Normally, completed in Excel, Tom's boss, Sam, wants to know if this can be done in Python.  If so, the code written for this election will be used for other, larger elections. 

Certifying this election includes the following tasks: 
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate received.
5. Determine the winner of the election based on the popular vote.

In addition, Sam would like an audit of the voter turnout by county. Specifically, he would like Sam to report on: 

* the voter turnout for each county (i.e. *total votes cast per county*),
* the percentage of all votes cast from each county, and
* the county with the highest turnout overall.

## Resources
The votes cast for this election were done so through 3 primary voting methods: 

1. Mail-in Ballots: *hand-counted*
2. Punchcards: *machine-counted*
3. Direct Recording Electronic reading machine: *computer-counted*

The results of these sources can be found in the comma delimited file, 
**election_results.csv**, located in the Resources file of this repository.  The data set includes: Ballot ID, County, and Candidate.

The software used, Python version 3.7.6 along with the code editor, Visual Studio Code version 1.49.3.

Let's see what we find....

## Election-Audit Results
The analysis of the election data shows that:

### **Overall Voter Turnout** 

* There were **369,111** votes cast in this election. The total votes was calculated after reading in the .csv file, initializing the variable total_votes to 0 and looping through the data adding a vote for each row read in:
 

```
# Read the csv and convert it into a list of dictionaries with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header; skips the header row
    header = next(reader)

    # For each row in the CSV file
    for row in reader:

        # Add to the total vote count; one method:total_votes = total_votes + 1, or
        total_votes +=1         
```

### **Voter Turnout by County**
* Votes were cast in the following counties: Arapahoe, Denver, Jefferson.  
 
***The code written to identify the list of counties included in these results and tally the vote count per county is as follows:***

	    # Decision statement that checks the county does not match any existing county in the county list.
        if county_name not in county_options:

            # Add the existing county to the list of counties.
            county_options.append(county_name)

            # Begin tracking the county's vote count.
            county_vote_dict[county_name] = 0

        # Add a vote to that county's vote count.
        county_vote_dict[county_name] += 1
        
 
       
* **Arapahoe County** had **24,801** votes cast representing **6.7%** of the vote. 
* **Denver County** had **306,055** votes cast representing **82.8%** of the vote.
* **Jefferson County** had **38,855** votes cast representing **10.5%** of the vote.

***The code written to calculate the percentage of total votes cast per county as well as identify the county with the largest turnout, as reported above, is as follows:***
               	
		# Repetition statement to get the county from the county dictionary.
		for county_name in county_vote_dict:        
				
			# Retrieve the county vote count; using new variable county_votes
			county_votes = county_vote_dict[county_name] 

       		# Calculate the percent of total votes for the county; using new variable county_percentage
       		county_percentage = float(county_votes) / float(total_votes) * 100
       		
       		# Decision statement to determine the winning county and get its vote count.
        	if (county_votes > county_tally):
            	county_tally = county_votes
            	county_lrgturnout = county_name

* The county with the largest voter turnout is clearly **Denver County** with **306,055** votes cast.


### **Candidate Results**

* Votes were cast for three (3) candidates.  They are Diana DeGette, Raymon Anthony Doane, and Charles Casper Stockham.  The code used to determine the candidates included in the results and how many votes each candidate won is as follows:

         # If the candidate does not match any existing candidate add it to the candidate list
         if candidate_name not in candidate_options:
          
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1 
               
1. **Diana DeGette** recieved **272,892** votes representing **73.8%** of the vote.
2. **Raymon Anthony Doane** recievd **11,606** votes representing **3.1%** of the vote.
3. **Charles Casper Stockham** recieved **85,213** votes representing **23.0%** of the vote.  

* The code written to calculate the percentage of total votes won by each candidate, as reported above, is as follows:
    

        # To calculate the percentage total votes won
        for candidate_name in candidate_votes:
        
        	# Retrieve vote count and percentage for each candidate
        	votes = candidate_votes.get(candidate_name)
        	vote_percentage = float(votes) / float(total_votes) * 100

	
* Clear winner of the election: **Diana DeGette** who won **73.8%** of the votes


The Python code for these summary results output to the terminal view as well as to a text file, named **election_analysis.txt** also included in this repository.  Please see the terminal screenshot below.  

**Screenshot of terminal output for Pyhton code: PyPoll_Challenge.py**

![Election_Ouput](./Resources/election_results_output.png)

## Election-Audit Summary
 
This code works beautifully for an isolated race like this one.  It reads in the names of the counties and the candidates rather than have the names hardcoded; this allows the code to work regardless of which county or which candidates the audit team is looking at.  It is flexible in that way. 

However, as it is written, the code reflects and is **limited by**, the input data, which in this case is only the Ballot ID, County and Candidate Name. So the code can be run for any race, but only for a very specific race.  As we know there are many different items on a ballot.

### Code Modifications
If additional data is included in the election results file, the code can be modified to perform similar summaries across multiple races and even measures and propositions by reading in additional lists to the ballot dictionaries.  Of course that would depend on how the results are captured: 

* All votes cast for all races in one field, as we see here, then an additional field would be needed, "ballot item identifier", to distinguish between the different races.  Something more like:

![New_input_data](./Resources/new_data_1.png)

In which case, the code would have to be modified to read in each of the Ballot Items and create a new dictionary for each item and then run the same analysis for each item. 
Dictionaries such as:

* Elections: president, senate, congress_1, congress_2, etc. (list of candidates)
* Measures: measure_A, measure_B, etc (boolean, yes/no)
* Propositions: prop__20, prop_30, etc. (boolean, yes/no)

OR

* Each Ballot Id is a unique entry with each of the possible Ballot Items being a separate field.  Something like:
![New_input_data2](./Resources/new_data_2.png)

This would be a cleaner format for the election data and ultimately easier to analyze.
One initial change in the code would be rather then skipping over the header row, **the header would be read in to get the keys for each dictionary representing each election item**. 

An easy way to read in this data and anlysize it would be to use the very popular, very powerful ***Pandas*** module. Initate the module when the others are imported (csv, os, etc)  ```import pandas as pd``` By utlizing this very helpful library of functions and short cuts, the expanded csv file can be read in as a data frame, akin to a very large and complex dictionary, and can be "grouped by" results for each series or list.  

Read in .cvs file similar to current code:
```election_results_to_load = os.path.join("Resources", "election_results.csv")```

Create a data frame
```election_data_df = pd.read_csv(election_results_to_load)```

Group by each of the ballot items, for example: District 1 Congressional race  
```congress_1 = election_data_df.groupby(["Congress_District_1"]).count()["Ballot_ID"]```
This statement creates a series (or list or array) where the names of the candidates becomes the index and tallies (or counts) the Ballot IDs.

Finally, a comestic modification needs to be incorporated, the results should be sorted in descending order to show winning result on top, rather than 

```Congress_1.sort_values(ascending=False)```

As the data is expanded, the scope of this current code needs to as well; incorporating pandas is an excellent way to achieve cleaner, easier to adapt code.