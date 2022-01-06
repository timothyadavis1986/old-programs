#! /usr/bin/env python
import datetime as dt

now = dt.date.today()
year = now.strftime('%Y')
day = now.strftime('%d')
month = now.strftime('%m')
monthA = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
milD = str(day) + monthA[int(month) - 1] + str(year)
print milD
