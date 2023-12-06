import re as regex

assign = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
    "zero":0,
    }

check = False
total = 0
reversedLine = ""
with open("codes.txt") as file:
    for line in file:
        leftResult = regex.findall(r"one|two|three|four|five|six|seven|eight|nine|zero|[0-9]", line)
        rightResult = regex.findall(r"eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|orez|[0-9]", line[::-1])
        print(rightResult)
        left = assign.get(leftResult[0])
        right = assign.get(rightResult[0][::-1])
        if left == None:
            left = leftResult[0]
        if right == None:
            right = rightResult[0][::-1]
        total = total + int((str(left)+ str(right)))

print(total)
