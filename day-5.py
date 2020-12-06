def inputFile(file):
    with open(file) as f:
        data = f.read().split("\n")
    f.close()
    return data

# Part 1
def calcSeatID (inputString):
    rowID = int(inputString[:7].replace("F", "0").replace("B", "1"), 2)
    colID = int(inputString[7:].replace("L", "0").replace("R", "1"), 2)
    return rowID * 8 + colID

def part1(file):
    data = inputFile(file)
    largestSeatID = -1
    for row in data:
        seatID = calcSeatID(row)
        if seatID > largestSeatID:
            largestSeatID = seatID
    return largestSeatID

# Part 2
def part2(file):
    data = inputFile(file)
    seatIDs = []
    for row in data:
        seatIDs.append(calcSeatID(row))
    seatIDs.sort()
    previousID = seatIDs[0]
    for seatID in seatIDs[1:]:
        if seatID - previousID != 1:
            return seatID - 1
        previousID = seatID

# Run
def main(file):
    print ("Part 1: {}".format(part1(file)))
    print ("Part 2: {}".format(part2(file)))

main("input-5.txt")