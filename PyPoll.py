#Add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a vairable to save the file to a path
file_to_save = os.path.join("analysis", "election_results.txt")

#initialize a total vote counter
total_votes = 0

#candidate options
candidate_options = []
#declare empty dictionary
candidate_votes = {}

#1: Create county list and county votes dictionary
county_list = []
county_votes = {}

#Winning candidate and Winning Count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#2: Track the largest county and county voter turnout
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # read the file object with the reader function
    file_reader = csv.reader(election_data)
    #read header row
    headers = next(file_reader)
    #print each row in the CSV file
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        #3. Extract county name from each row
        county_name = row[1]


        #if the candidate does not match any existing candidate..
        if candidate_name not in candidate_options:
            #add it to the list of candidates
            candidate_options.append(candidate_name)
            #begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        #4a: Write an if statement that checks that the county 
        # does not match any existing county in the county list
        if county_name not in county_list:
            # 4b add existing county to the list of counties
            county_list.append(county_name)
            # 4c begin tracking the county's vote count
            county_votes[county_name] = 0
        #5. Add a vote to that county's vote count    
        county_votes[county_name] += 1


#save the results to our text file
with open(file_to_save, "w") as txt_file:
    #print final vote count to terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #save final cote count to the text file
    txt_file.write(election_results)

    county_header = (f"County Votes:\n")
    print(county_header)
    txt_file.write(county_header)

    #6a Write a for loop to get the county from the county dictionary
    for county_name in county_votes:
        #6b Retrieve the county vote count
        votes = county_votes[county_name]
        #6c calculate the percentage of votes for the county
        vote_percentage = float(votes) / float(total_votes) * 100
        #6d print county results to the terminal
        county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results, end="")
        #6e save the county votes to a text file
        txt_file.write(county_results)
        #6f write an if statement to determine the winning county and get its vote count
        if (votes > winning_county_count) and (vote_percentage > winning_county_percentage):
            winning_county_count = votes
            winning_county_percentage = vote_percentage
            winning_county = county_name
    #7 Print the county with the largest turnout to the terminal 
    winning_county_summary = (
        f"--------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"--------------------------\n")
    print(winning_county_summary, end="")
    #8 Save the county with the largest turnout to a text file
    txt_file.write(winning_county_summary)
    

    #Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of candidate
        votes = candidate_votes[candidate_name]
        # calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # to do: print out each candidate's name, vote count, and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #print each dndiate, their voter count, and percentage to the terminal
        print(candidate_results)
        #save candidate results to our text file
        txt_file.write(candidate_results)
        
        #Determine winning vote count and candidate 
        #Determine if votes is greater than winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #and, set winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
    #print winning candidate's results to the terminal
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
    print(winning_candidate_summary)
    # save winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)




















