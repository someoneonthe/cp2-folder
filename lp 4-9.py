import random
ainum = int(random.randint(1,20))
mnum = int(input("chose a number between 1 and 20:"))
if 0 > mnum < 20:
    mnum = int(input("I SAID BETWEEN 1 AND 20:"))
if mnum == ainum:
    print ("You win :) ai number was: ", ainum)
else:
    print ("you lose  ai num: ", ainum)