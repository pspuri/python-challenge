import os
import csv

file_to_read = "budget_data.csv"
file_to_output = "Budget_Analysis.txt"

#open and read the file 
with open (file_to_read) as fin_data:
    reader = csv.reader(fin_data)
    
    #skip first line 
    next(reader)
    
    #define variables as lists
    profit_loss = []
    date = []
    p_l_change = []
    
    #iterate through the columns and sum 
    
    for row in reader:
        profit_loss.append(int(row[1]))
        date.append(row[0])
        
        #print("Budget Analysis")
        #print("-----------------------------------")
        #print("Total Months:", len(date))
        #print("Total Profit and Loss: $", sum(profit_loss))
        
    # go through and find difference between profit and loss in each month, and average, and maximum and minimum change and dates 
    
    for i in range(1,len(profit_loss)):
        p_l_change.append(profit_loss[i] - profit_loss[i-1])
        avg_p_l_change = sum(p_l_change) / len(p_l_change)
        
        max_p_l_change = max(p_l_change)
        min_p_l_change = min(p_l_change)
        
        max_p_l_change_date = str(date[p_l_change.index(max(p_l_change))])
        min_p_l_change_date = str(date[p_l_change.index(min(p_l_change))])
        
    print("Budget Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total Profit and Loss: $", sum(profit_loss))
    print("Avereage Profit and Loss Change: $", round(avg_p_l_change))
    print("Greatest Increase in Profit and Loss:", max_p_l_change_date,"($", max_p_l_change,")")
    print("Greatest Decrease in Profit and Loss:", min_p_l_change_date,"($", min_p_l_change,")")
    
with open(file_to_output, "w") as txt_file:
    
    #print(type(len(date)))
    
    total_months = len(date)
    #print(type(total_months))
    
    total_months = str(total_months)
    #print(type(total_months))
    
    total_profit_loss = sum(profit_loss)
    total_profit_loss = str(total_profit_loss)
    
    average_p_l_change = round(avg_p_l_change)
    average_p_l_change = str(average_p_l_change)
    
    txt_file.write("Budget Analysis")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Total Months: " + total_months)
    txt_file.write("\n")
    txt_file.write("Total Profit and Loss Change: $ " + total_profit_loss)
    txt_file.write("\n")
    txt_file.write("Avereage Profit and Loss Change: $ " + average_p_l_change)
    txt_file.write("\n")
    txt_file.write("Greatest Increase in Profit and Loss: " + str(max_p_l_change_date) + "  $ " + str(max_p_l_change))
    txt_file.write("\n")
    txt_file.write("Greatest Decrease in Profit and Loss: " + str(min_p_l_change_date) + "  $  " + str(min_p_l_change))
    txt_file.close()
                   
                   
                   
    