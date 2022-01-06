#! /usr/bin/env python
month = input("What is the month in numbers ")
day = input("what is the day ")
year = input("what is the year ")
monthA = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
if (day >= 31):
    while (day >= 31):
        day -= 31
        month += 1


if (month > 12):
    while (month > 12):
        month -= 12
        year += 1
        
    
day = str(day)
year = str(year)
mil = ""
mil = mil + day
mil = mil + monthA[month - 1]
mil = mil + year
print mil
