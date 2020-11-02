#Author: Zach Page
#Date: 10/12/2020
#Filename: inAction2.py

import csv

#insert CSV name

with open('TimeSheet.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

#insert new CSV name

    with open('NewTimeSheet.csv', 'w') as new_file:

#insert headline names
        
        fieldnames = []
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()
    
    for line in csv_reader:
        csv_writer.writerow(line)
