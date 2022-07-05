import os
import csv

# path to collect data from Resources folder
pyPoll_csv = os.path.join("Resources", "election_data.csv")

# file to hold the analysis
pyPollOutput = os.path.join ("analysis", "election_data.txt")

# define total votes initially as zero
totalVotes = 0
candidates = []
candidateVotes = {}
winnnigCandidate = ""
winningCount = 0 


# open the pyPoll_csv file and then read inside the csv file

with open(pyPoll_csv) as poll_data:
    csvreader = csv.reader(poll_data, delimiter = ",")

    # reads the header row and then the next goes to the first row of data
    header = next(csvreader)

    for row in csvreader:
        totalVotes += 1

        # check and see if candidate is in candidates list
        if row[2] not in candidates:
            # so this checks to see if the candidate is not in the candidats list, if it is not, then it will add
            candidates.append(row[2])

            # start adding the value to the dictionary as well
            # start the count of the votes at 1
            candidateVotes[row[2]] = 1
        
        else:
            candidateVotes[row[2]] += 1
        
        # candidateVotesOutput = float(f"{candidateVotes[row[2]]}")

    voteOutput = ""

    for candidate in candidateVotes:
        votes = candidateVotes.get(candidate)
        votesPercent = (float(votes)/float(totalVotes)) * 100

        # voteOutput = adds the first candidate info in candidateVotes and then we put \n to go onto the next row and add ont the next candidate until we have stopped running loop
        voteOutput += f"{candidate}: {votesPercent: .3f}% ({candidateVotes[row[2]]})\n"

        if votes > winningCount:
            winningCount = votes
            winnnigCandidate = candidate 
    
    winnnigCandidateOutput = f"Winner: {winnnigCandidate}"


output = f"\nElection Results\n----------------------------------\nTotal Votes: {totalVotes}\n----------------------------------\n{voteOutput}----------------------------------\n{winnnigCandidateOutput}\n----------------------------------" 
print(output)

with open(pyPollOutput, 'w') as textFile:
    textFile.write(output) 
    





 
