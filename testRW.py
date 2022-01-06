#! /usr/bin/env python
import testRef as ref
import testMod as mod
import sys
import os

os.system('clear')
ref.main()
usrIn = int(input("\n::"))
x = 0
media = []
while(usrIn != 0):
    if(usrIn == 1):
        media.append(mod.main())
        usrIn = int(input("\n::"))

    elif(usrIn == 2):
        while(x < len(media)):
            print str(media[x][0]) + " " + media[x][1] + " " + media[x][2]
            x+=1

        x = 0
        usrIn = int(input("\n::"))

    elif(usrIn == 3):
        opened = False
        try:
            myFile = open("testRWFile.txt", "w+")
            while(x < len(media)):
                myFile.write(str(media[x][0]) + "," + media[x][1] + "," + media[x][2] + "+")
                x+=1

            x = 0
            myFile.write("/")
            opened = True
        except:
            print "Something didn't happen that should have"
        
        if(opened):
            myFile.close()

        usrIn = int(input("\n::"))

    elif(usrIn == 4):
        contents = None
        try:
            myFile = open("testRWFile.txt", "r")
            contents = myFile.read()
            myFile.close()

        except:
            print "Something didn't happen that should have"
        
        usrIn = int(input("\n::"))
        while len(contents) > 1:
            if contents[0] != "/":
                index = contents.find(",")
                tempM = contents[0:index]
                contents = contents[index + 1::]
                tempMA = [tempM]
                index = contents.find(",")
                tempM = contents[0:index]
                contents = contents[index + 1::]
                tempMA.append(tempM)
                index = contents.find("+")
                tempM = contents[0:index]
                contents = contents[index + 1::]
                tempMA.append(tempM)
                media.append(tempMA)


    elif(usrIn == 9):
        os.system('clear')
        ref.main()
        usrIn = int(input("\n::"))

