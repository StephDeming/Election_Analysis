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

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)










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
