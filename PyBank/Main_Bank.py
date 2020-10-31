import os
import csv
import sys

#Read and import csv from Resources folder
PyBank_budget_data=os.path.join("Resources/PyBank_budget_data.csv")
month_count =0
total=0
max_value= -999999999
max_month= ""
min_value= 999999999
min_month= ""
total_change= []
last_profit=0

def average(lst): 
    return sum(lst) / len(lst) 

with open (PyBank_budget_data, 'r') as csv_file:
    
    csv_reader=csv.reader(csv_file, delimiter=',')
    csv_header=next(csv_reader)


    for row in csv_reader:
        profit = int(row[1])
        month = row[0]

        if month_count ==0:
            last_profit=profit

        else:
            #print("calculate change")
            change= profit-last_profit
            total_change.append(change)

            if min_value > change:
                min_value=change
                min_month=month

            if max_value < change:
                max_value=change
                max_month=month



            #update last_profit
            last_profit=profit

        total=total+profit
        month_count += 1

print("Financial Analysis")
print("------------------------------")
print(f'Total Months: {month_count}')
print(f'Total: ${total: 0,.0f}')
print(f'Average: ${average(total_change): 0,.0f}')
print(f'Greatest Increase: {max_month}, ${max_value: 0,.0f}')
print(f'Greatest Decrease: {min_month}, ${min_value: 0,.0f}')

stdoutOrigin=sys.stdout 
txtPath = os.path.join("Analysis/financial_analysis.txt")
sys.stdout = open(txtPath, "w")
print("Financial Analysis")
print("------------------------------")
print(f'Total Months: {month_count}')
print(f'Total: ${total: 0,.0f}')
print(f'Average: ${average(total_change): 0,.0f}')
print(f'Greatest Increase: {max_month}, ${max_value: 0,.0f}')
print(f'Greatest Decrease: {min_month}, ${min_value: 0,.0f}')