result = 0
f = open('2015Day2Text.txt')

for line in f:
    numbers = []
    for word in a_string.split():
       if word.isdigit():
          numbers.append(int(word))

    print(numbers)








