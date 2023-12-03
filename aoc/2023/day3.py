import itertools

with open("aoc/2023/day3.data") as f:
    data = f.read()

line_length = len(data.split("\n")[0])

data = data.replace("\n", "")

data = "." * line_length + data + "." * line_length


# Part 1

index = itertools.count(line_length)

sum_of_part_numbers = 0

while True:

    pos = next(index)

    if data[pos] in "1234567890":

        start = pos
        end = pos+1

        while data[next(index)] in "1234567890":
            end += 1
        

        search_context = data[start-1 - line_length :end+1 - line_length] + data[start-1:end+1] + data[start-1 + line_length:end+1 + line_length]

        for char in "1234567890.":
            search_context = search_context.replace(char, "")

        if len(search_context) > 0:
            sum_of_part_numbers += int(data[start:end])

    if pos == len(data) - line_length:
        break

print(f"Part 1: {sum_of_part_numbers}")


# Part 2

index = itertools.count(line_length)

sum_of_indexes = 0
gear_list = []

while True:

    pos = next(index)

    if data[pos] in "1234567890":

        start = pos
        end = pos+1

        while data[next(index)] in "1234567890":
            end += 1
        
        for i in range(start-1-line_length, end+1-line_length):
            if data[i] == "*":
                gear_list.append({"gear": int(data[start:end]), "star_pos": i})
        
        for i in range(start-1, end+1):
            if data[i] == "*":
                gear_list.append({"gear": int(data[start:end]), "star_pos": i})

        for i in range(start-1+line_length, end+1+line_length):
            if data[i] == "*":
                gear_list.append({"gear": int(data[start:end]), "star_pos": i})

    if pos == len(data) - line_length:
        break

for i in range(len(data)+line_length):
    
    short_list = [x["gear"] for x in gear_list if x["star_pos"] == i]

    if len(short_list) == 2:
        sum_of_indexes += short_list[0] * short_list[1]

print(f"Part 2: {sum_of_indexes}")
