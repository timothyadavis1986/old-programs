#! /usr/bin/env python3

import weight as etm
import os

os.system('clear')
print("""This program is to calculate your weight on earth and on the moon.\n
We'll assume that you gain a certain amount of weight each year.\n
You will be asked for your starting earth weight.\n
Then you will be asked how many years you think you will be on the moon.\n
Finally you will be asked how much weight you think you will gain each year.\n""")
print("First let get introduced\n")
name = input("What is your name? ")
print("\nHi {}, it's nice to meet you\n".format(name))
earthWeight = int(input("What is your earth weight in pounds? "))
totalYears = int(input("\nHow many years do you think you will be on the moon? "))
gain = int(input("\nHow much earth weight in pounds do you think you will gain each year? "))
moonWeight = int(earthWeight * .165)
print("\nYour starting earth weight is {} lbs and your starting moon weight is {} lbs".format(earthWeight, moonWeight))
for year in range(1, totalYears + 1):
    earthWeight += gain
    moonWeight = int(etm.earthToMoon(earthWeight))
    print("\nIn year {}, your earth weight is {} lbs and your moon weight is {} lbs.".format(year, earthWeight, moonWeight))

etm.yeah()
