# Author: Guðjón Ingi Valdimarsson

import itertools

def inputFile(file):
    with open(file) as f:
        data = f.read().split("\n")
    f.close()
    data = [int(i) for i in data]
    return data

# Part 1
def part1(file):
    data = inputFile(file)
    preamble = 25
    for i in range(preamble, len(data)):
        searchValue = data[i]
        searchList = data[i-preamble:i]
        combList = list(itertools.combinations(searchList, 2))
        combCounter = len(combList)
        for comb in combList:
            if sum(comb) == searchValue:
                break
            combCounter -= 1
        if combCounter == 0:
            return searchValue
    return "None found"

# Part 2
def part2(file):
    data = inputFile(file)
    value = part1(file)
    for index, number in enumerate(data):
        sumOfNumbers = number
        smallest =  number
        largest = number
        for number2 in data[index + 1:]:
            sumOfNumbers += number2
            if sumOfNumbers > value:
                break
            if number2 > largest:
                largest = number2
            elif number2 < smallest:
                smallest = number2
            if sumOfNumbers == value:
                return smallest + largest
    return "None found"


# Run
def main(file):
    print ("Part 1: {}".format(part1(file)))
    print ("Part 2: {}".format(part2(file)))

main("input-9.txt")