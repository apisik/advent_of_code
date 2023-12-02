import re

limits = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

with open("aoc/2023/day2.data") as f:
    data = f.read().splitlines()


# Part 1

sum_of_ids = 0

for index, line in enumerate(data):

    for key, value in limits.items():
        
        pattern = re.compile(rf"([0-9]+) {key}")
        matches = pattern.findall(line)

        game_number  = int(line[5:].split(":")[0])

        if len(matches) > 0:
            for match in matches:
                if int(match) > value:
                    game_number = None
                    break

        if game_number is None:
            break
    
    if game_number is not None:
        sum_of_ids += game_number

print(f"Part 1: {sum_of_ids}")    


# Part 2

sum_of_powers = 0

for index, line in enumerate(data):

    limits["red"] = 0
    limits["green"] = 0
    limits["blue"] = 0

    for key, value in limits.items():
        
        pattern = re.compile(rf"([0-9]+) {key}")
        matches = pattern.findall(line)

        if len(matches) > 0:
            for match in matches:
                if int(match) > limits[key]:
                    limits[key] = int(match)

    sum_of_powers += limits["red"] * limits["green"] * limits["blue"]

print(f"Part 2: {sum_of_powers}")
