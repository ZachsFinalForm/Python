#Author: Zach Page
#Date: 11/02/2020
#Filename: inAction2.py

import csv

with open('.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new .csv', 'w') as new_file:
        fieldnames = ['']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()
    
    for line in csv_reader:
        csv_writer.writerow(line)
