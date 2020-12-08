def inputFile(file):
    with open(file) as f:
        data = f.read().replace(".", "").replace(" ", "").replace("bags", "").replace("bag", "").split("\n")
    f.close()
    data = [line.split("contain") for line in data]
    data = [[line[0], line[1].split(",")] for line in data]
    return data

# Part 1
def part1(file):
    data = inputFile(file)
    bagDict = {}
    for line in data:
        for bag in line[1]:
            try:
                bagDict[bag[1:]].append(line[0])
            except KeyError:
                bagDict[bag[1:]] = [line[0]]
    return len(part1Rec(bagDict, "shinygold"))

def part1Rec(bagDict, searchBag):
    try:
        if bagDict[searchBag] == []:
            return set()
    except KeyError:
        return set()
    counter = set()
    for bag in bagDict[searchBag]:
        counter = counter | part1Rec(bagDict, bag)
    return set(bagDict[searchBag]) | counter

# Part 2
def part2(file):
    data = inputFile(file)
    countDict = {}
    for line in data:
        for bag in line[1]:
            if bag != "noother":
                try:
                    countDict[line[0]].update({bag[1:]: int(bag[0])})
                except KeyError:
                    countDict[line[0]] = {bag[1:]: int(bag[0])}
    return part2Rec(countDict, "shinygold")

def part2Rec(countDict, searchBag):
    try:
        countDict[searchBag]
    except KeyError:
        return 0
    counter = 0
    for bag in countDict[searchBag]:
        current = countDict[searchBag][bag]
        counter += current + (current * part2Rec(countDict, bag))
    return counter

# Run
def main(file):
    print ("Part 1: {}".format(part1(file)))
    print ("Part 2: {}".format(part2(file)))

main("input-7.txt")