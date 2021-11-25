#2015 Day 1 Puzzle

f = open("2015Day1Text")
puzzleInput = f.read()
groundFloor = 0
basementCounter = 1


for i in puzzleInput:
    if i == '(':
        groundFloor += 1
    elif i == ')':
        groundFloor -= 1


for i in puzzleInput:
    if i == ')':
        break
    elif i == '(':
        basementCounter += 1


print(groundFloor)
print(basementCounter)

