# Modules
import os
import csv

#create two lists (initalize)
changeslist = []
monthlist = []

# Set path for file
csvpath = os.path.join("Resources","budget_data.csv")

# set variables to 0
total = 0
months = 0
sum_change = 0
previous = 0

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    firstrow = next(csvreader)
    firstvalue = float(firstrow[1])
    months = months +1 
    total = total + firstvalue
    previous = firstvalue

    # Loop through the rows (don't count header row)
    for row in csvreader:

        total = total +float(row[1])
        months = months + 1

        #--------
        #Should only be done if months <1
        change = float(row [1])- previous
        changeslist.append (change)
        monthlist.append (row[0])
    
        #sum_change= sum_change + change
        #print(row [0],change)
        #Find the maximum change
        #Find minimum change

    # set previous to the current row
        previous = float(row[1])
    #---------
        

    # What does it mean by change?
    #So change is current month - previous month
average = sum (changeslist)/ len(monthlist)
average = round(average,2)
maxchange = max(changeslist)
minchange = min(changeslist)
greatestmonthindex=changeslist.index(maxchange)
greatestmonth = monthlist[greatestmonthindex]
worstmonthindex=changeslist.index(minchange)
worstmonth = monthlist[worstmonthindex]


#Print results to text files
output=os.path.join("output.txt")
with open(output, "w") as textfile:
        parameterfile=textfile
        print("Financial Analysis") #normal print
        print("Financial Analysis", file=textfile) #printtofile
        print(f"Total months: {months}")
        print(f"Total months: {months}",file=textfile)
        print(f"Total: {total}")
        print(f"Total: {total}",file=textfile)
        print(f"Average: ${average}")
        print(f"Average: ${average}",file=textfile)
        print(f"Greatest Increase in Profits: {maxchange},Greatest Month: {greatestmonth}")
        print(f"Greatest Increase in Profits: {maxchange},Greatest Month: {greatestmonth}",file=textfile)
        print(f"Greatest Decrease in Profits: {minchange},Worst Month: {worstmonth}")
        print(f"Greatest Decrease in Profits: {minchange},Worst Month: {worstmonth}",file=textfile)



# #Print results to text files
# output=os.path.join("output.txt")
# with open(output, "w") as textfile:
#         parameterfile=textfile
#         print("Financial Analysis") #normal print
#         print("Financial Analysis", file=textfile) #printtofile
    
        # txt_file.write(f"Total months: {months}")
        # txt_file.write(f"Total: {total}")
        # txt_file.write(f"Average: {average}")
        # txt_file.write(f"Greatest Increase in Profits: {maxchange},Greatest Month: {greatestmonth}")
        # txt_file.write(f"Greatest Decrease in Profits: {minchange},Worst Month: {worstmonth}")

