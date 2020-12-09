# Author: Guðjón Ingi Valdimarsson

def input(file):
    with open(file) as f:
        inputList = f.read().split("\n")
        inputList = [int(i) for i in inputList]
        inputList.sort()
    return inputList

# Part 1
def searchInput(inputList):
    n = len(inputList)-1
    for i in range(0, n):
        for j in range(n, 0, -1):
            lower = inputList[i]
            upper = inputList[j]
            if lower + upper == 2020:
                return (lower, upper)

def part1(file):
    data = input(file)
    lower, upper = searchInput(data)
    return lower * upper

print(part1("input-1.txt"))


# Part 2
def searchInput3(inputList):
    n = len(inputList)-1
    for i in range(0, n):
        for j in range(n, 0, -1):
            for k in range (1, n):
                lower = inputList[i]
                upper = inputList[j]
                mid = inputList[k]
                if lower + upper + mid == 2020:
                    return (lower, upper, mid)

def part2(file):
    data = input(file)
    lower, upper, mid = searchInput3(data)
    return lower * upper * mid

print(part2("input-1.txt"))