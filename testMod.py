#! /usr/bin/env python

def main():
    mediaType = int(input("Is this:\n1: VIDEO\n2: GAME\n::"))
    if mediaType == 1:
        mediaName = str(input("What is the movies Name?\n::"))
        mediaGen = str(input("What is the movies genre?\n::"))

    elif mediaType == 2:
        mediaName = str(input("What is the games name?\n::"))
        mediaGen = str(input("What system is this for?\n::"))
    
    media = [mediaType, mediaName, mediaGen]
    return media

if __name__ == "__main__":
    main()
