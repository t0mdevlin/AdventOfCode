for i in range(100):
    output = ""
    if i % 3 == 0:
        output += "fizz"
    elif i % 5 == 0:
        output += "buzz"
    else:
        output += str(i)

    print(output)