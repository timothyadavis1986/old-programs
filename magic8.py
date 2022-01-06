#! /usr/bin/env python3

import BoringStuffPg64 as BSP64
import random as r

myNum = r.randint(1,9)
life = BSP64.getAnswer(myNum)
print(life)

#BSP64.getAnswer()
