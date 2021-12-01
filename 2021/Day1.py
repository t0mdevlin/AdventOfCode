f = open("./files/day1.txt")

increaseCount = 0
previousLine = 0
lineIndex = 0

for line in f:
    line = int(line)
    output = ""
    if lineIndex == 0:
        output = str(line) + " - First Line, no previous measurement."

    else:
        if line > previousLine:
            increaseCount += 1
            output = str(line) + " - increased"
        elif line < previousLine:
            output = str(line) + " - decreased"

    lineIndex += 1
    previousLine = line
    #print(str(lineIndex)+" - "+output)

print("part 1: "+str(increaseCount))
