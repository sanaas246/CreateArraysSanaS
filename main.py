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
for mult in range(20, 80, 4):
    multFour.append(mult)

# 7 
evenli = []
for evenNum in range(0, 100, 2):
    evenli.insert(len(evenli) + 1, evenNum)
print(evenli)

# # 8
# colors_str = "red,orange,yellow,green,blue,indigo,violet"
# for color in colors_str:
#     print(f"{color}")

# # 9
# cities_str = "Edmonton;Calgary;Vancouver;Saskatoon;Winnipeg"
# for city in cities_str:
#     print(f"{city}")