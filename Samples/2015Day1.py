#2015 Day 1 Puzzle

f = open("2015Day1Text")
puzzleInput = f.read()
groundFloor = 0
basement = 0
counter = 0


for i in puzzleInput:
    if i == '(':
        groundFloor += 1
    elif i == ')':
        groundFloor -= 1


for i in puzzleInput:
    if i == ')':
       basement += 1
    elif i == '(':
        basement -= 1

    if basement == -1:
        print(counter)
        break
    counter += 1

print(groundFloor)


