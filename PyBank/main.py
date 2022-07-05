import os
import csv

# path to collect data from Resources folder
pyBank_csv = os.path.join("Resources", "budget_data.csv")

# file to hold the analysis
pyBankOutput = os.path.join ("analysis", "budget_data.txt")

# define total months initially as zero
# define total profit loss
# initialize a list of monthly changes 
# months list so that we can keep a track of what month the greatestIncrease and greatestDecrease take place
# "" is for month and 0 is the value of greatestIncrease or greatestDecrease, respesctively 
totalMonths = 0
totalProfitLoss = 0
monthlyChanges = []
months = []

# open the pyBank_csv file and then read inside the csv file

with open(pyBank_csv) as budget_data:
    csvreader = csv.reader(budget_data, delimiter = ",")

    # reads the header row and then the next goes to the first row of data
    # first row has index 0 = Date and index 1 = Profit/Losses
    header = next(csvreader)

    # move down to the first row to get the previous profit/loss
    firstRow = next(csvreader)

    totalMonths += 1
    totalProfitLoss += float(firstRow[1])

    # establish what the previous profit/loss was for the previous month
    # set previous profit/loss = first profit/loss we see
    # index 1 = Profit/Loss
    previousProfitLoss = float(firstRow[1])

    for row in csvreader:
        totalMonths += 1
        totalProfitLoss += float(row[1])
    
        # calculate the net change
        netChange = float(row[1]) - previousProfitLoss

        # now you need to store that netChange so that you do not lose it
        # push those values into monthlyChanges list
        monthlyChanges.append(netChange)

        # add the first month that a change occurred 
        # month is in index = 0 
        months.append(row[0])

        # update the previousProfitLoss
        previousProfitLoss = float(row[1])

    averageChange = (sum(monthlyChanges))/(len(monthlyChanges))

    greatestIncrease = [months[0],monthlyChanges[0]]
    greatestDecrease = [months[0],monthlyChanges[0]]

    # use for loop to calculate the index of the greatest and least monthly change
    for m in range(len(monthlyChanges)):
        # calculate greatestIncrease and greatestDecrease
        if monthlyChanges[m] > greatestIncrease[1]:
            # if this is the case then that values becomes the new greatest increase
            greatestIncrease[1] = monthlyChanges[m]
            # update the month
            greatestIncrease[0] = months[m]
            
        if monthlyChanges[m] < greatestDecrease[1]:
            # if this is the case then that values becomes the new greatest decrease
            greatestDecrease[1] = monthlyChanges[m]
            # update the month
            greatestDecrease[0] = months[m]

output = f"\nFinancial Analysis\n----------------------------------\nTotal Months: {totalMonths}\nTotal: ${totalProfitLoss: .0f}\nAverage Change: ${averageChange: .2f}\nGreatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]: .0f})\nGreatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]: .0f})" 
print(output)

with open(pyBankOutput, 'w') as textFile:
    textFile.write(output) 
    





 
