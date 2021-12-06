from sys import argv
from math import prod

def readlines(fname):
    with open(fname) as f:
        lines = f.readlines()
        return lines

def get_horizontal_depth():
    lines = readlines(argv[1])
    cur_horizontal = 0
    cur_depth = 0
    for line in lines:
        cmd, amt = line.split()
        amt = int(amt)
        if cmd == "forward":
            cur_horizontal += amt
        elif cmd == "up":
            cur_depth -= amt
        elif cmd == "down":
            cur_depth += amt
    return [cur_horizontal, cur_depth]

def get_horizontal_depth_with_aim():
    lines = readlines(argv[1])
    cur_horizontal = 0
    cur_depth = 0
    cur_aim = 0
    for line in lines:
        cmd, amt = line.split()
        amt = int(amt)
        if cmd == "forward":
            cur_horizontal += amt
            cur_depth += cur_aim * amt
        elif cmd == "up":
            cur_aim -= amt
        elif cmd == "down":
            cur_aim += amt
    return [cur_horizontal, cur_depth]

print(prod(get_horizontal_depth_with_aim()))