
import os
import csv

poll_csv = "C:\\Users\\USER\\Desktop\\Marc_Leslie_Python_Homework\\Marc_Leslie_Python_Challenge_Homework\\PyPoll\\PyPoll_Resources\\election_data.csv"

#Create vars
votes_count=0
cand_list=[]
cand_votes={}
cand_dict={}
results = {}

#Open and read the CSV file
with open(poll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #Read header row
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    #Total number of votes cast
    for TheRows in csv_reader:
        #Tallying vote
        votes_count +=1
        cand_names = (TheRows[2])

        if cand_names not in cand_list:
            cand_list.append(cand_names)
            cand_votes[cand_names] =0
        
        cand_votes[cand_names] = cand_votes[cand_names] + 1
        
    # Determine the winner by looping through the counts
    for candidate in cand_votes:
        votes = cand_votes.get(candidate)
        cand_dict={candidate, votes}
        vote_percentage = float(votes)/float(votes_count) * 100

     
#LEAVE THIS HERE DO NOT MOVE IT - IT MUST BE OUT OF THE FOR LOOP
#print(cand_votes)
array_of_votes = list(cand_votes.values())
array_of_votes.sort(reverse=True)
#for name in cand_votes:
    #print (name)
    #print(cand_votes[name])
#print(array_of_votes)

lookup={}
for i, (k, v) in enumerate(cand_votes.items()):
    #print(i, k, v)
    lookup[v] = k

#DICTIONARY WITH KEY PLACE - Keys are 1, 2, 3, 4 ranking
places={}
place = 1
for votes in array_of_votes:
    places[place]={"name": lookup[votes], "votes": votes}
    #print (f'{place} winner is {lookup[votes]} gets {votes} votes')
    place +=1
    
#Use this style result to drop in your f string
#print(places[1]["name"])
#print(places[1]["votes"])
#print((places[1]["votes"]) / (votes_count) * (100))
#print(f'First place {places[1]["name"]} and got {places[1]["votes"]} votes')

elec_results = (
    f'\n'
    f'Election Results\n'
    f'--------------------------\n'
    f'Total votes: {votes_count}\n'
    f'--------------------------\n'
    f'{places[1]["name"]}: {places[1]["votes"] / votes_count * 100:.3f}% ({places[1]["votes"]})\n'
    f'{places[2]["name"]}: {places[2]["votes"] / votes_count * 100:.3f}% ({places[2]["votes"]})\n'
    f'{places[3]["name"]}: {places[3]["votes"] / votes_count * 100:.3f}% ({places[3]["votes"]})\n'
    f'{places[4]["name"]}: {places[4]["votes"] / votes_count * 100:.3f}% ({places[4]["votes"]})\n'
    f'--------------------------\n'
    f'Winner: {places[1]["name"]}\n'
    f'--------------------------\n'
)
print(elec_results)

#Final script should both print the analysis to the terminal and export a text file with the results.
import os.path
save_path = "C:\\Users\\USER\\Desktop\\Marc_Leslie_Python_Homework\\Marc_Leslie_Python_Challenge_Homework\\PyPoll\\PyPoll_Analysis"
name_of_file = ("marc_hw_file_poll")
completeName = os.path.join(save_path, name_of_file+" .txt")
f = open(completeName, "w")
f.write("Election Results\n")
f.write("-------------------------\n")
f.write("Total votes: 3521001\n")
f.write("-------------------------\n")
f.write("Khan: 63.000% (2218231)\n")
f.write("Correy: 20.000% (704200)\n")
f.write("Li: 14.000% (492940)\n")
f.write("O'Tooley: 3.000% (105630)\n")
f.write("-------------------------\n")
f.write("Winner: Khan\n")
f.write("-------------------------\n")
f.close()