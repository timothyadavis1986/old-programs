#! /usr/bin/env python3
import baccarat

play = "yes"
wins = 0
total = 0
while("y" in play or "Y" in play):
    wins += baccarat.main()
    total += 1
    play = input("Would you like to play again yes or no:: ")

print(str(wins) + " Wins & " + str(total - wins) + " Losses out of " + str(total))
