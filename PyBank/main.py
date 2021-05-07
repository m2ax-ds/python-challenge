import os 
import csv

# counter for rows 
count_rows=0
#total_PL=0
PL_col =[]
PL_date=[]
date_row=[]
#max_PL =[]
#min_PL = []
# file path 
csv_path= "resources/budget_data.csv"
# open csv file and restore in csv_reader 
with open(csv_path, 'r') as csv_file: 
    csv_reader= csv.reader(csv_file , delimiter=',')
    #ignore first row 
    csv_header=next(csv_reader)
    for row in csv_reader:
        count_rows+=1
        PL_col.append(int(row[1]))
        PL_date.append(row[0])
    PL_col_total= sum(PL_col)
    average_PL=int((PL_col[-1] - PL_col[0])/len(PL_col))
    inex_max=PL_col.index(max(PL_col))
    inex_min=PL_col.index(min(PL_col))

print ('Financial Analysis ')
print("-------------------------------------")     
print(f' Total months : {count_rows}')
print(f' Total : ${PL_col_total} ')
print(f' Average  Change: ${average_PL}')
print(f' Greatest Increase in Profits: {PL_date[inex_max] }  $({max(PL_col)}) ')
print(f' Greatest Decrease in Profits: {PL_date[inex_min] }  $({min(PL_col)}) ')

txt_path="analysis/analysis_PyBank.txt"
with open(txt_path, 'w') as PyBank_result:
    #txt_writer=txt_writer(PyBank_result)
    PyBank_result.write('Financial Analysis ')
    PyBank_result.write('\n------------------------------------- ')
    PyBank_result.write(f' \nTotal months : {count_rows}')
    PyBank_result.write(f' \nTotal : ${PL_col_total} ')
    PyBank_result.write(f' \nAverage  Change: ${average_PL}')
    PyBank_result.write(f' \nGreatest Increase in Profits: {PL_date[inex_max] }  $({max(PL_col)}) ')
    PyBank_result.write(f' \nGreatest Decrease in Profits: {PL_date[inex_min] }  $({min(PL_col)}) ')
