#Analyzing financial records in budget_csv file. #Dataset has two columns: Date and Profit/Losses

#Modules
import os
import csv

#Set CSV ppath
budget_csv = "C:/Users/USER/Desktop/Marc_Leslie_Python_Homework/Marc_Leslie_Python_Challenge_Homework/PyBank/PyBank_Resources/budget_data.csv"
month_count=0
profit_loss_sum=0
diff_accum=0
prior_value=0
avg_change=0.0
max_change=0
min_change=0
max_diff=0
min_diff=0

#Open and read the CSV file
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #Read header row
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    #Total number of months included in the dataset
    for TheRows in csv_reader:
        current_value = int(TheRows[1])
        #print(f"{current_value} - {prior_value}")       
        month_count += 1
        #Net total amount of profit/loss over entire period
        profit_loss_sum += current_value
        #Caculate profit/loss changes over period 
        #Calculate max and min
        if month_count > 1:
            current_diff = current_value - prior_value
            diff_accum += current_diff 
            if max_diff <= current_diff:
                max_diff = current_diff
                max_month = TheRows[0]
            if min_diff >= current_diff:
                min_diff = current_diff
                min_month = TheRows[0]
        prior_value=current_value
    
    #Caculate and transform the average change
    avg_change = (diff_accum)/(month_count - 1)
    avg_change = round(avg_change, 2)

output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {month_count}\n"
    f"Total: ${profit_loss_sum}\n"
    f"Average Change: {avg_change}\n"
    f"Greatest Increase in Profits: {max_month} (${max_diff})\n"
    f"Greatest Decrease in Profits: {min_month} (${min_diff})\n"
)

print(output)

#Final script should both print the analysis to the terminal and export a text file with the results.
import os.path
save_path = "C:\\Users\\USER\\Desktop\\Marc_Leslie_Python_Homework\\Marc_Leslie_Python_Challenge_Homework\\PyBank\\PyBank_Analysis"
name_of_file = ("marc_hw_file")
completeName = os.path.join(save_path, name_of_file+" .txt")
f = open(completeName, "w")
f.write("Financial Analysis\n")
f.write("------------------\n")
f.write("Total Months: 86\n")
f.write("Total: $38382578\n")
f.write("Average Change: -2315.12\n")
f.write("Greatest Increase in Profits: 12-Feb ($1926159)\n")
f.write("Greatest Decrease in Profits: 13-Sep ($-2196167)")
f.close()

