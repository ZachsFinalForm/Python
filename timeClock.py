#Author: Zach Page
#Date: 11/10/2020
#Filename: timeClock.py


#import utility class
import utilities as u

## Adding hours or minutes or seconds to datetime
from datetime import datetime, timedelta
 
## Original datetime
datetime_original = datetime(year=2020, month=11, day=10)
print("\nOriginal date: ", datetime_original, "\n")


hoursWorked = u.hoursWorked('TimeSheet.csv')

for i in hoursWorked:
    x = i.split(',')
    print(x[2])

input("Hit any key to proceed")
 
## Adding Hours
hours_to_add = 12
datetime_new = datetime_original + timedelta(hours = hours_to_add)
print("After adding hours: ", datetime_new, "\n")

minutesWorked = u.minutesWorked('TimeSheet.csv')

for i in minutesWorked:
    x = i.split(',')
    print(x[3])

input("Hit any key to proceed")

 
## Adding Minutes
minutes_to_add = 45
datetime_new = datetime_new + timedelta(minutes = minutes_to_add)
print("After adding minutes: ", datetime_new, "\n")

secondsWorked = u.secondsWorked('TimeSheet.csv')

for i in secondsWorked:
    x = i.split(',')
    print(x[4])

input("Hit any key to proceed")

 
## Adding Seconds
seconds_to_add = 33
datetime_new = datetime_new + timedelta(seconds = seconds_to_add)
print("After adding seconds: ", datetime_new, "\n")

microsceondsWorked = u.microsecondsWorked('TimeSheet.csv')

for i in microsecondsWorked:
    x = i.split(',')
    print(x[5])

input("Hit any key to proceed")

 
## Adding Microseconds
microseconds_to_add = 12345
datetime_new = datetime_new + timedelta(microseconds = microseconds_to_add)
print("After adding microseconds: ", datetime_new, "\n")



