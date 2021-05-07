import os
import csv

vote_count=0
khan_vote=[]
correy_vote=[]
li_vote=[]
tooley_vote=[]
vote_results=[]
csv_path="resources/election_data.csv"
with open (csv_path) as election_data:
    poll_data= csv.reader(election_data, delimiter=',')
    csv_header=next(poll_data)
    for row in poll_data:
        vote_count+=1
        vote_results.append(row[2])
    #results={i:vote_results.count(i) for i in vote_results}
results_khan= vote_results.count("Khan")
results_corey= vote_results.count("Correy")
results_li= vote_results.count("Li")
results_tooley= vote_results.count("O'Tooley")
final_results={'Khan':results_khan,'Correy': results_corey,'Li': results_li,"O'Tooley":results_tooley}
winner= max(final_results,key=final_results.get)
print('Election Results \n-------------------------')
print(f'Total Votes: {int(vote_count)}\n-------------------------')
print(f'Khan: {round(((results_khan/vote_count)*100),3)}% ({results_khan})')
print(f'Correy: {round(((results_corey/vote_count)*100),3)}% ({results_corey})')
print(f'Li: {round(((results_li/vote_count)*100),3)}% ({results_li})')
print(f"O'Tooley: {round(((results_tooley/vote_count)*100),3)}% ({results_tooley})")
print('-------------------------')

print(f'Winner : {winner}')
#print (results_khan,results_corey,results_li,results_tooley)

txt_path="analysis/analysis_PyPoll.txt"
with open(txt_path, 'w') as PyPoll_result:
    
    PyPoll_result.write('Election Results')
    PyPoll_result.write('\n------------------------------------- ')
    PyPoll_result.write(f'\nTotal Votes: {int(vote_count)}\n-------------------------')
    PyPoll_result.write(f'\nKhan: {round(((results_khan/vote_count)*100),3)}% ({results_khan})')
    PyPoll_result.write(f'\nCorrey: {round(((results_corey/vote_count)*100),3)}% ({results_corey})')
    PyPoll_result.write(f'\nLi: {round(((results_li/vote_count)*100),3)}% ({results_li})')
    PyPoll_result.write(f"\nO'Tooley: {round(((results_tooley/vote_count)*100),3)}% ({results_tooley})")
    PyPoll_result.write('\n------------------------------------- ')
    PyPoll_result.write(f'\nWinner : {winner}')
    PyPoll_result.write('\n------------------------------------- ')