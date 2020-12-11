# Author: Guðjón Ingi Valdimarsson

import itertools

def inputFile(file):
    with open(file) as f:
        data = f.read().split("\n")
    f.close()
    data = [int(i) for i in data]
    data.append(0)
    data.sort()
    data.append(data[-1] + 3)
    return data

# Part 1
def part1(file):
    data = inputFile(file)
    return part1Solve(data)

def part1Solve(data):
    onesCount = 0
    threesCount = 0
    for index in range(1, len(data)):
        difference = data[index] - data[index-1]
        if difference == 3:
            threesCount += 1
        elif difference == 1:
            onesCount += 1
        elif difference == 2:
            pass
        else:
            raise Exception
    return onesCount * threesCount

# Part 2
def part2(file):
    data = inputFile(file)
    removableList = [set()] # List of sets that contain removable elements
    counter = 1             # Final value counter that is returned
    removableSetCounter = 0 # Designates what set is being added to
    for i in range(1, len(data) - 1):
        diffLow = data[i] - data[i - 1]     # Diff for element and element -1
        diffHigh = data[i + 1] - data[i]    # Diff for element and element +1
        diffMid = data[i + 1] - data[i - 1] # Diff for element -1 and element +1
        if diffLow < 3 and diffHigh < 3 and diffMid < 4: # If element is removable
            removableList[removableSetCounter].add(data[i]) 
        else:
            if removableList[removableSetCounter] != set(): # Check if a new set should be created
                removableList.append(set())
                removableSetCounter += 1

    removableList.pop() # Remove extra empty set from back
    for removableSet in removableList:
        setCounter = 0
        combs = []
        # Get all combinations of the removable set
        [combs.extend(list(itertools.combinations(list(removableSet), r))) for r in range(len(removableSet)+1)]

        for comb in combs:
            newData = data.copy()
            for val in comb:
                newData.remove(val) # Generate a new list without the elements in the combination
            try:
                part1Solve(newData) # Test if the new data works
                setCounter += 1
            except Exception:
                pass
        counter *= setCounter # Multiply count of working sets with total working sets
    return counter

# Run
def main(file):
    print ("Part 1: {}".format(part1(file)))
    print ("Part 2: {}".format(part2(file)))

main("input-10.txt")