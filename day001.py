# https://adventofcode.com/2021/day/1#part2

input_file = 'day001.txt'
measurements = []

with open(input_file, 'r') as r:
    lines = r.readlines()
    for line in lines:
        measurement = int(line.strip())
        measurements.append(measurement)

def analyse_depth_increase(measurements):
    increases = 0
    if len(measurements) < 2:
        return increases
    for index in range(1, len(measurements)):
        increases += 1 if measurements[index] > measurements[index - 1] else 0
    return increases

print(analyse_depth_increase(measurements))

def analyse_depth_increase_three_measurement_window(measurements):
    increases = 0
    if len(measurements) < 4:
        return increases
    for index in range(1, len(measurements)-2):
        increases += 1 if sum(measurements[index:index+3]) > sum(measurements[index-1:index-1+3]) else 0
    return increases

print(analyse_depth_increase_three_measurement_window(measurements))