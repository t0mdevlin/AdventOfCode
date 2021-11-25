f = open('2015Day1Text')
contents = f.read()
print("Floor:", contents.count('(') - contents.count(')'))

# Part Two
change = {'(': 1, ')': -1}

floor = 0
position = 1
for c in contents:
    if c in change:
        floor += change[c]
    if floor == -1:
        print("Basement entered at position:", position)
        break
    position += 1