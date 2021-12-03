# https://adventofcode.com/2021/day/3

input_file = 'day003.txt'
lines = open(input_file, 'r').readlines()
lines = [line.strip() for line in lines]


def part1():
    processed_list = [0 for i in range(0, len(lines[0]))]
    lines_list = []
    for line in lines:
        line_list = [1 if i == '1' else -1 for i in list(line)]
        processed_list = [item1 + item2 for item1, item2 in zip(processed_list, line_list)]
        lines_list.append(line_list)
    most_common = [1 if i > 0 else 0 for i in processed_list]
    least_common = [1 if i < 0 else 0 for i in processed_list]

    most_common_dec = int(''.join([str(i) for i in most_common]), 2)
    least_common_dec = int(''.join([str(i) for i in least_common]), 2)
    return most_common_dec * least_common_dec

# mc, lc, mc_list, lc_list, lines_list = part1()
# print(mc * lc)
# print(mc_list)
# print(lc_list)
# print(lines)
# print(lines_list)
# print(sum([i[4] for i in lines_list]))

# Part 2
def part2_find_ox_rating():
    elements = len(lines[0])
    #print(elements)
    source_list = lines.copy()
    for idx in range(elements):
        if len(source_list) == 1:
            break

        #print(idx)
        lines_of_1 = []
        lines_of_0 = []
        for line in source_list:
            if line[idx] == '1':
                lines_of_1.append(line)
            else:
                lines_of_0.append(line)
        if len(lines_of_1) >= len(lines_of_0):
            source_list = lines_of_1.copy()
        else:
            source_list = lines_of_0.copy()
    return source_list[0]

def part2_find_co2_rating():
    elements = len(lines[0])
    #print(elements)
    source_list = lines.copy()
    for idx in range(elements):
        if len(source_list) == 1:
            break
        #print(idx)
        lines_of_1 = []
        lines_of_0 = []
        for line in source_list:
            if line[idx] == '1':
                lines_of_1.append(line)
            else:
                lines_of_0.append(line)
        if len(lines_of_1) < len(lines_of_0):
            source_list = lines_of_1.copy()
        else:
            source_list = lines_of_0.copy()

    return source_list[0]

print(part1())
ox_rating = int(part2_find_ox_rating(),2)
co2_rating = int(part2_find_co2_rating(),2)
print(co2_rating * ox_rating)