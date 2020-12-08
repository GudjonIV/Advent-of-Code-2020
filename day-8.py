import copy

def inputFile(file):
    with open(file) as f:
        data = f.read().split("\n")
    f.close()
    return [line.split(" ") for line in data]

# Part 1
def part1(file):
    data = inputFile(file)
    insPointer = 0
    insList = []
    acc = 0
    while insPointer != (len(data) - 1):
        if insPointer not in insList:
            insList.append(insPointer)
        else:
            break
        line = data[insPointer]
        if line[0] == "nop":
            insPointer += 1
        elif line[0] == "acc":
            acc += int(line[1])
            insPointer += 1
        elif line[0] == "jmp":
            insPointer += int(line[1])
    return acc

# Part 2
def part2(file):
    data = inputFile(file)
    return part2Rec(data, 0, "", False)

def part2Rec(data, pointer, instStr, testBool):
    if pointer >= len(data):
        return 0
    if " " + str(pointer) + " " in instStr:
        raise Exception("Loop found")
    instStr += " " + str(pointer) + " "
    if data[pointer][0] == "jmp" and not testBool:
        try:
            return part2Rec(data, pointer + 1, instStr, True)
        except Exception:
            return part2Rec(data, pointer + int(data[pointer][1]), instStr, False)
    elif data[pointer][0] == "jmp":
        return part2Rec(data, pointer + int(data[pointer][1]), instStr, testBool)

    elif data[pointer][0] == "nop" and not testBool:
        try:
            return part2Rec(data, pointer + int(data[pointer][1]), instStr, True)
        except Exception:
            return part2Rec(data, pointer + 1, instStr, False)
    elif data[pointer][0] == "nop":
        return part2Rec(data, pointer + 1, instStr, testBool)

    else:
        return int(data[pointer][1]) + part2Rec(data, pointer + 1, instStr, testBool)

# Run
def main(file):
    print ("Part 1: {}".format(part1(file)))
    print ("Part 2: {}".format(part2(file)))

main("input-8.txt")