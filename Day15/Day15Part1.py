from collections import defaultdict

# Start Pos + Time (value to offset) % Number of positions

file_name = '/Users/karlobrien/projects/python/AdventOfCode2016/Day15/input.txt'
data = open(file_name).readlines()

def parse_line(line):
    breakup = line.split(' ')
    num_pos = int(breakup[3])
    start_pos = int(breakup[11][0])
    return (start_pos, num_pos)

def is_open_position(start_pos, time, num_pos):
    return (start_pos + time) % num_pos

def calc_for_disk(disk, id, start_time):
    num_pos = disk[1]
    start_pos = disk[0]
    disk_time = id + start_time
    return is_open_position(start_pos, disk_time, num_pos)

def apply_cycle(status, start_time):
    return max([calc_for_disk(status[i], i, start_time) for x, i in enumerate(status)])

def parse_input(items):
    status = defaultdict(tuple)
    disk_num = 1
    for line in data:
        item = parse_line(line)
        status[disk_num] = item
        disk_num += 1
    return status

input_data = parse_input(data)
start_time = 0
while True:
    if apply_cycle(input_data, start_time) == 0:
        print start_time
        break
    start_time += 1
