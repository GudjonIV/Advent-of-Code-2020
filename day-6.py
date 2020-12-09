# Author: Guðjón Ingi Valdimarsson

def inputFile(file):
    with open(file) as f:
        data = f.read().split("\n\n")
    f.close()
    return data

# Part 1
def part1(file):
    data = inputFile(file)
    data = [set(line.replace("\n", "")) for line in data]
    counterList = [len(line) for line in data]
    return sum(counterList)

# Part 2
def part2(file):
    data = inputFile(file)
    data = [line.split("\n") for line in data]
    counterList = []
    for line in data:
        groupSet = {chr(i) for i in range(97, 123)}
        for answers in line:
            answers = set(answers)
            groupSet = groupSet.intersection(answers)
        counterList.append(len(groupSet))

    return sum(counterList)

# Run
def main(file):
    print ("Part 1: {}".format(part1(file)))
    print ("Part 2: {}".format(part2(file)))

main("input-6.txt")