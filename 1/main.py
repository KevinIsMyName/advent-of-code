import sys


def readlines(fname):
    with open(fname) as f:
        lines = f.readlines()
        return lines


def count_increases():
    lines = readlines(sys.argv[1])
    num_increases = 0
    for l in range(1, len(lines)):
        if int(lines[l-1]) < int(lines[l]):
            num_increases += 1

    print(num_increases)

def count_sum3_window_increase():
    def sum3_window(li, start):
        return sum(li[start:start + 3])

    lines = [int(i) for i in readlines(sys.argv[1])]
    num_increases = 0
    for l in range(1, len(lines) - 2):
        if sum3_window(lines, l - 1) < sum3_window(lines, l):
            num_increases += 1

    print(num_increases)
    
count_increases()
count_sum3_window_increase()

