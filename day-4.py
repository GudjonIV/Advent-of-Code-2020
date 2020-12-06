import re

# Part 1
def input(file):
    with open(file) as f:
        data = f.read().split("\n\n")
    f.close()
    data = [entry.replace("\n", " ").split(" ") for entry in data]
    for i in range(len(data)):
        data[i] = {data[i][j][:3]: data[i][j][4:] for j in range(len(data[i]))}
    return data

def part1(file):
    data = input(file)
    validCount = 0
    for entry in data:
        if len(entry) == 8 or (len(entry) == 7 and "cid" not in entry):
            validCount += 1
    return validCount

print (part1("input-4.txt"))

# Part 2
def part2(file):
    data = input(file)
    validCount = 0
    for entry in data:
        # Check if lengths are valid
        if (7 == len(entry) and "cid" not in entry) or len(entry) == 8:
            # Birth year
            if 1920 <= int(entry["byr"]) <= 2002:
                # Issue year
                if 2010 <= int(entry["iyr"]) <= 2020:
                    # Expiration year
                    if 2020 <= int(entry["eyr"]) <= 2030:
                        # Hair color
                        if entry["hcl"][0] == "#" and re.match("[a-f0-9]", entry["hcl"][1:]):
                            # Eye color
                            if entry["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                                # Passport id
                                if entry["pid"].isnumeric() and len(entry["pid"]) == 9:
                                    # Heights
                                    if entry["hgt"][-2:] == "in":
                                        if 59 <= int(entry["hgt"][:-2]) <= 76:
                                            validCount += 1
                                    elif entry["hgt"][-2:] == "cm":
                                        if 150 <= int(entry["hgt"][:-2]) <= 193:
                                            validCount += 1
    return validCount

print (part2("input-4.txt"))