#2015 Day 2 Puzzle

result = 0
ribbon = 0
f = open('2015Day2Text.txt')

for line in f:
    l, w, h = line.split('x')
    l, w, h = int(l), int(w), int(h)

    #paper
    sum1 = l * w
    sum2 = w * h
    sum3 = h * l
    extra = min(sum1, sum2, sum3)

    calc = 2*sum1 + 2*sum2 + 2*sum3 + extra
    result += calc

    #ribbon
    r = min(l+l+w+w, l+l+h+h, w+w+h+h)
    bow = l * w * h
    ribbon += (r + bow)

print(result)
print(ribbon)
