

# https://adventofcode.com/2021/day/2
input_file = 'day002.txt'

def part1():
    horizondal = 0
    depth = 0

    with open(input_file, 'r') as r:
        lines = r.readlines()
        for line in lines:
            direction, value = line.strip().split(' ')
            value = int(value)
            horizondal += value if direction == 'forward' else 0
            depth += value if direction == 'down' else 0
            depth -= value if direction == 'up' else 0

    return horizondal, depth

horizondal, depth = part1()
print(horizondal, depth, horizondal*depth)

def part2():
    horizondal = 0
    depth = 0
    aim = 0

    with open(input_file, 'r') as r:
        lines = r.readlines()
        for line in lines:
            direction, value = line.strip().split(' ')
            value = int(value)
            aim += value if direction == 'down' else 0
            aim -= value if direction == 'up' else 0

            horizondal += value if direction == 'forward' else 0
            depth += (value * aim) if direction == 'forward' else 0

    return horizondal, depth

horizondal, depth = part2()
print(horizondal, depth, horizondal*depth)
