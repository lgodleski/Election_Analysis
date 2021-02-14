# The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

#Add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a vairable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter
total_votes = 0

#candidate options
candidate_options = []
#declare empty dictionary
candidate_votes = {}

#Winning canddiate and Winning Count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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

        #if the candidate does not match any existing candidate..
        if candidate_name not in candidate_options:
            #add it to the list of candidates
            candidate_options.append(candidate_name)
            #begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

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
    



















