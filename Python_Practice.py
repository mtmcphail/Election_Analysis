counties = ["Arapahoe","Denver","Jefferson"]

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

#for county in counties:
#   print(county)

#for i in range(len(counties)):
#    print(counties[i])



counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)


for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

#printing out the item or key, variable pair
# for key, value in counties_dict.items(): 
#    print(key, value)

#printing out dictionary items or key, value pair using items
#county and voters are variable we assign for the Key and Value in the dictionary for the for-loop
for county, voters in counties_dict.items():
#    print(county, "County has", voters, "registered voters.")
    print(county + " County has " + str(voters) + " registered voters.")


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

# to get just the values - registered voters - from each dictionary in the list
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

# to get just the key - county - from each dictionary in the list
for county_dict in voting_data:
    print(county_dict['county'])


for county_dict in voting_data:
    print(county_dict['registered_voters'])

# f String output
#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}

#for county, voters in counties_dict.items():
#    print(f"{county} County has {voters} registered voters.")


# Multi line F String with formatting {value:width, precision}
#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("Wh at is the total number of votes in the election? "))
#message_to_candidate = (
#    f"You received {candidate_votes:,} number of votes. "
#    f"The total number of votes in the election was {total_votes:,}. "
#    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

#print(message_to_candidate)

#Skill Drill

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(f"{county} County has {voters:,} registered voters.")


#skill Drill
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(f"{county_dict['county']} County has {county_dict['registered_voters']:,} registered voters.")


