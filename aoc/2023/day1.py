with open("aoc/2023/day1.data") as f:
    data = f.read().splitlines()

# Part 1

running_total = 0

for line in data:

    while line[0] not in "1234567890":
        line = line[1:]

    while line[-1] not in "1234567890":
        line = line[:-1]

    running_total += int(line[0]+line[-1])

print("Part 1: ", running_total)


# Part 2

running_total = 0

of = open("aoc/2023/day1.debug", "w")

for line in data:

    number_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0
    }

    stack = []

    while len(line) > 0:

        if line[0] in "1234567890":
            stack.append(int(line[0]))
            line = line[1:]
        else:
            for key, value in number_dict.items():
                if line.startswith(key):
                    stack.append(value)
                    break
            line = line[1:]

    running_total += int(str(stack[0]) + str(stack[-1]))

print("Part 2: ", running_total)
