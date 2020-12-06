# Part 1
def input(file):
    with open(file) as f:
        inputList = f.read()
        inputList = inputList.split("\n")
    return inputList

def part1(file):
    data = input(file)
    counter = 0
    for i in range(len(data)):
        line = data[i].split(" ")
        low, high = line[0].split("-")
        letter = line[1][0]
        text = line[2]
        counts = text.count(letter)
        if counts >= int(low) and counts <= int(high):
            counter += 1
    return counter
    
print(part1("input-2.txt"))


# Part 2
def part2(file):
    data = input(file)
    counter = 0
    for i in range(len(data)):
        line = data[i].split(" ")
        first, second = line[0].split("-")
        letter = line[1][0]
        text = line[2]
        if (text[int(first) - 1] == letter) != (text[int(second) - 1] == letter):
            counter += 1
    return counter

print (part2("input-2.txt"))