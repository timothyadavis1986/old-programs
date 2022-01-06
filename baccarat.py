#! /usr/bin/env python3
import random as rand
import baccaratValue as bv

cards = []

def fillCards():
    cards.append("A of spades")
    cards.append("2 of spades")
    cards.append("3 of spades")
    cards.append("4 of spades")
    cards.append("5 of spades")
    cards.append("6 of spades")
    cards.append("8 of spades")
    cards.append("9 of spades")
    cards.append("10 of spades")
    cards.append("J of spades")
    cards.append("Q of spades")
    cards.append("K of spades")
    cards.append("A of clubs")
    cards.append("2 of clubs")
    cards.append("3 of clubs")
    cards.append("4 of clubs")
    cards.append("5 of clubs")
    cards.append("6 of clubs")
    cards.append("7 of clubs")
    cards.append("8 of clubs")
    cards.append("9 of clubs")
    cards.append("10 of clubs")
    cards.append("J of clubs")
    cards.append("Q of clubs")
    cards.append("K of clubs")
    cards.append("A of hearts")
    cards.append("2 of hearts")
    cards.append("3 of hearts")
    cards.append("4 of hearts")
    cards.append("5 of hearts")
    cards.append("6 of hearts")
    cards.append("7 of hearts")
    cards.append("8 of hearts")
    cards.append("9 of hearts")
    cards.append("10 of hearts")
    cards.append("J of hearts")
    cards.append("Q of hearts")
    cards.append("K of hearts")
    cards.append("A of diamonds")
    cards.append("2 of diamonds")
    cards.append("3 of diamonds")
    cards.append("4 of diamonds")
    cards.append("5 of diamonds")
    cards.append("6 of diamonds")
    cards.append("7 of diamonds")
    cards.append("8 of diamonds")
    cards.append("9 of diamonds")
    cards.append("10 of diamonds")
    cards.append("J of diamonds")
    cards.append("Q of diamonds")
    cards.append("K of diamonds")

def card():
    return rand.randint(0, len(cards) - 1)

def cardValue(arg, arg2):
    newArg = int(bv.main(arg)) + int(bv.main(arg2))
    while (newArg > 9):
        newArg = newArg - 10
    return newArg

def reducing(arg):
    while (arg > 9):
        arg = arg - 10
    return arg

def printMethod(arg1, arg2, arg3):
    return "{:<15s}{:<15s}{:>15d}".format(arg1, arg2, arg3)

def printMethod2(arg1, arg2, arg3, arg4):
    return "{:<15s}{:<15s}{:<15s}{:>15d}".format(arg1, arg2, arg3, arg4)

def main():
    if len(cards) < 6:
        fillCards()
    player1Card = cards.pop(card())
    bank1Card = cards.pop(card())
    player2Card = cards.pop(card())
    bank2Card = cards.pop(card())
    player3Card = ""
    bank3Card = ""
    pCV = cardValue(player1Card, player2Card)
    bCV = cardValue(bank1Card, bank2Card)
    print(str(printMethod(player1Card, player2Card, pCV)) + "\n")
    print(str(printMethod(bank1Card, bank2Card, bCV)) + "\n")
    if(pCV == 0 or pCV == 1):
        player3Card = cards.pop(card())
        pCV = reducing(pCV + cardValue(player3Card, "None"))
        if(bCV <= 3):
            bank3Card = cards.pop(card())
            bCV = reducing(bCV + cardValue(bank3Card, "None"))
    elif(pCV == 2 or pCV == 3):
        player3Card = cards.pop(card())
        pCV = reducing(pCV + cardValue(player3Card, "None"))
        if(bCV <= 4):
            bank3Card = cards.pop(card())
            bCV = reducing(bCV + cardValue(bank3Card, "None"))
    elif(pCV == 4 or pCV == 5):
        player3Card = cards.pop(card())
        pCV = reducing(pCV + cardValue(player3Card, "N"))
        if(bCV <= 5):
            bank3Card = cards.pop(card())
            bCV = reducing(bCV + cardValue(bank3Card, "N"))
    elif(pCV == 6 or pCV == 7):
        if(bCV <= 6):
            bank3Card = cards.pop(card())
            bCV = reducing(bCV + cardValue(bank3Card, "N"))
    elif(pCV == 8):
        if(bCV <= 2):
            bank3Card = cards.pop(card())
            bCV = reducing(bCV + cardValue(bank3Card, "N"))
    elif(pCV == 9):
        if(bCV <= 3):
            bank3Card = cards.pop(card())
            bCV = reducing(bCV + cardValue(bank3Card, "N"))

    print(str(printMethod2(player1Card, player2Card, player3Card, pCV)) + "\n")
    print(str(printMethod2(bank1Card, bank2Card, bank3Card, bCV)) + "\n")
    new = 0
    if(pCV > bCV):
        print("!!!!!!!!!!!!!!!!!!!!!!!!YOU WINS!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        new = 1
    return new

if __name__ == "__main__":
    main()
