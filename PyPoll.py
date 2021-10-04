#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

# Assign a variable for the file to load and the path.

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes=0
#1st step for loop new list(candidate)
candidate_options=[]
#dictionary for candidate votes
candidate_votes={}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    

    #print each row in the CSV file.
    for row in file_reader:
    
        
       # Print each row in the CSV file.
     for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            #add each candidate as key/begin tracking vote count
            candidate_votes[candidate_name] = 0
            #add a vote to candidate's count
        candidate_votes[candidate_name]+=1
        #use for loop to iterate through candidates list
for candidate_name in candidate_votes:
    #retrieve vote count
    votes=candidate_votes[candidate_name]
    #calculate percentage of vote count
    vote_percentage = (votes / total_votes) * 100
    # Determine winning vote count and candidate
# 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
     # 2. If true then set winning_count = votes and winning_percent =
     # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
     # 3. Set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)         
 #print using f string
         #print(f"{candidate_name}:recieved {vote_percentage}% of the vote.")
    #  To do: print out the winning candidate, vote count and percentage to
#   terminal.
print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
# Print the candidate list.
print(candidate_votes)
  









#Using the with statement open the file as a text file.
# with open(file_to_save,"w") as txt_file:
# #write some date to the file.
# # outfile.write("Hello World")
# #Write title
#     txt_file.write("Counties in the Election\n-----------------\n")
    
# # Write three counties to the file.
#     txt_file.write("Arapahoe\nDenver\nJefferson")
# #close the file
# outfile.close()
