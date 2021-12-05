
input_file = 'day005.txt'

lines = open(input_file, 'r').readlines()

filtered_inputs = []
diagonal_inputs = []

for line in lines:
    line = line.strip().replace('>', '').replace(' ','')
    part1, part2 = line.split('-')
    x1, y1 = part1.split(',')
    x2, y2 = part2.split(',')
    if x1 == x2 or y1 == y2:
        match = 0 if x1 == x2 else 1
        filtered_inputs.append(((int(x1), int(y1)), (int(x2), int(y2)), match))
    else:
        diagonal_inputs.append(((int(x1), int(y1)), (int(x2), int(y2))))

input_dicts = dict()

for input in filtered_inputs:
    end1, end2, row_col = input
    if row_col == 0:
        x = end1[0]
        start, finish = sorted([end1[1], end2[1]])
        for y in range(start, finish + 1):
            input_key = f"{x}_{y}"
            if input_key in input_dicts:
                input_dicts[input_key] += 1
            else:
                input_dicts[input_key] = 1
    else:
        y=end1[1]
        start, finish = sorted([end1[0], end2[0]])
        for x in range(start, finish + 1):
            input_key = f"{x}_{y}"
            if input_key in input_dicts:
                input_dicts[input_key] += 1
            else:
                input_dicts[input_key] = 1

intersections = 0
for key in input_dicts:
    if input_dicts[key] > 1:
        intersections += 1

print(intersections)

def get_x(start, finish, step):
    for x in range(start, finish, step):
        yield x
    return None

def get_y(start, finish, step):
    for y in range(start, finish, step):
        yield y
    return None


for end1, end2 in diagonal_inputs:
    x1, y1 = end1
    x2, y2 = end2
    #print(end1, end2)

    if x1 < x2:
        x_step = 1
        x_start, x_finish = x1, x2 + 1
    else:
        x_step = -1
        x_start, x_finish = x1, x2 - 1

    if y1 < y2:
        y_step = 1
        y_start, y_finish = y1, y2 + 1
    else:
        y_step = -1
        y_start, y_finish = y1, y2 - 1

    x_gen = get_x(x_start, x_finish, x_step)
    y_gen = get_y(y_start, y_finish, y_step)

    while True:
        try:
            x = next(x_gen)
            y = next(y_gen)
            input_key = f"{x}_{y}"
            #print(end1, end2, input_key)
            if input_key in input_dicts:
                # print(f"adding 1 by {input_key} now value in {input_dicts[input_key]}")
                input_dicts[input_key] += 1
            else:
                input_dicts[input_key] = 1

        except StopIteration as exc:
            break


intersections = 0
for key in input_dicts:
    if input_dicts[key] > 1:
        intersections += 1

print(intersections)