lineNums = []
total = 0
temp = ""
with open("codes.txt") as file:
    for line in file:
        for char in line: 
            if char.isdigit():
                lineNums.append(char)
        temp = temp + lineNums[0] + lineNums[len(lineNums)-1]
        lineNums = []
        total = int(total + int(temp))
        temp = ""

print(total)
