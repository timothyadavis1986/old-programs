#! /usr/bin/env python3

def main(card):
    if "A" in card:
        return int(1)
    elif "2" in card:
        return int(2)
    elif "3" in card:
        return int(3)
    elif "4" in card:
        return int(4)
    elif "5" in card:
        return int(5)
    elif "6" in card:
        return int(6)
    elif "7" in card:
        return int(7)
    elif "8" in card:
        return int(8)
    elif "9" in card:
        return int(9)
    else:
        return int(0)

if __name__ == "__main__":
    main()
