with open("aoc/2023/day4.data") as f:
    data_raw = f.read().splitlines()


# Part 1

total_points = 0

for line in data_raw:
    
    data = line.split(":")[1]

    winning_nums = [int(x) for x in data.split("|")[0].split(" ") if x != ""]
    my_nums = [int(x) for x in data.split("|")[1].split(" ") if x != ""]


    score = 0

    for num in winning_nums:
        if num in my_nums:
            if score > 0:
                score = score * 2
            else:
                score = 1

    total_points += score


print("Part 1:", total_points)
            

# Part 2


multipliers = [1] * len(data_raw)

total_points = 0

for index, line in enumerate(data_raw):
    
    data = line.split(":")[1]

    winning_nums = [int(x) for x in data.split("|")[0].split(" ") if x != ""]
    my_nums = [int(x) for x in data.split("|")[1].split(" ") if x != ""]

    score = 0

    for num in winning_nums:
        if num in my_nums:
            score += 1

    for _ in range(multipliers[index]):
        for i in range(score):
            multipliers[index + 1 + i] += 1

    total_points += score * multipliers[index]

print("Part 2:", total_points)
