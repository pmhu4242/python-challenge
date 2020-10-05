import os 
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

total_months = 0
total_profit_loss=0
total_change=0
last_profit_loss=0
recent_change=0
greatest_profit=0
greatest_profit_month=''
greatest_loss=0
greatest_loss_month=""
avgchange=0
profit_changes = []


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)
        # months = len(list(csvreader)) + 1
        total_months +=1
        total_profit_loss += int(row[1]) 


        if total_months==1:
            last_profit_loss=int(row[1])
        else:
            recent_change=int(row[1])-last_profit_loss
            total_change+=recent_change
            last_profit_loss=int(row[1])
        
        if recent_change > greatest_profit:
            greatest_profit=recent_change
            greatest_profit_month=str(row[0])
        
        elif recent_change < greatest_loss:
            greatest_loss = recent_change
            greatest_loss_month= str(row[0])

avgchange = "%2.f" % (total_change/(total_months-1))

output_path = os.path.join("Analysis", "pybank_results.txt")
with open(output_path, 'w') as txtfile:

    print(f'Financial Analysis', file=txtfile)
    print(f'Financial Analysis')
    print('----------------------------------', file=txtfile)
    print('----------------------------------')
    print(f'Total Month Count: {total_months}', file=txtfile)
    print(f'Total Month Count: {total_months}')
    print(f'Total Profit/Loss: ${total_profit_loss}', file=txtfile)
    print(f'Total Profit/Loss: ${total_profit_loss}')
    print(f'Average Change: ${avgchange}', file=txtfile)
    print(f'Average Change: ${avgchange}')
    print(f'Greatest Increase in Profits: {greatest_profit_month} (${greatest_profit}) ', file=txtfile)
    print(f'Greatest Increase in Profits: {greatest_profit_month} ${greatest_profit} ')
    print(f'Greatest Decrease in Profits: {greatest_loss_month} (${greatest_loss})', file=txtfile)
    print(f'Greatest Decrease in Profits: {greatest_loss_month} ${greatest_loss}')


   
       


    
# The total number of months included in the dataset
   
# The net total amount of "Profit/Losses" over the entire period

# The net total amount of "Profit/Losses" over the entire period

# The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period