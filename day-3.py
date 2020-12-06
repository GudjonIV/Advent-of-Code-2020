# Part 1
def input(file):
    with open(file) as f:
        inputList = f.read()
        inputList = inputList.split("\n")
    return inputList

def part1(file):
    data = input(file)
    lineLen = len(data[0])
    treesHit = 0
    xCord = 0
    for line in data[1:]:
        xCord = (xCord + 3) % lineLen
        if line[xCord] == "#":
            treesHit += 1
    return treesHit

print (part1("input-3.txt"))

# Part 2
def part2(file, right, down):
    data = input(file)
    lineLen = len(data[0])
    treesHit = 0
    xCord = 0
    for line in data[down::down]:
        xCord = (xCord + right) % lineLen
        if line[xCord] == "#":
            treesHit += 1
    return treesHit

inputFile = "input-3.txt"
one = part2(inputFile, 1, 1)
two = part2(inputFile, 3, 1)
three = part2(inputFile, 5, 1)
four = part2(inputFile, 7, 1)
five = part2(inputFile, 1, 2)
print (one * two * three * four * five)