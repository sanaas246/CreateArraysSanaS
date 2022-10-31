# Create Arrays Practice

import random 

# 1
months = ["January", "June", "July"]

# 2
joyli = []
for joy in range(700):
    joyli.append("joy")

# 3
sevenli = []
for sevens in range(500):
    sevenli.append("7")

# 4
randomNums = []
for rand in range(5000):
    randomNums.append(random.randint(0,100))

# 5
randomInts = []
for rand in range(300):
    randomInts.append(random.randint(0,40))

# 6
multFour = []
for mult in range(20, 801, 4):
    multFour.append(mult)

# 7 
evenli = []
for evenNum in range(100, 9, -2):
    evenli.append(evenNum)

# 8
colors_str = "red,orange,yellow,green,blue,indigo,violet"
colors_str.split(",")

# 9
cities_str = "Edmonton;Calgary;Vancouver;Saskatoon;Winnipeg"
cities_str.split(";")

# 10
names = []
loop = True
while loop:
    usernames = input("Please enter a name or type 'done': ")
    if usernames != "done":
        names.append(usernames)
    else:
        print("thanks")
        loop = False

