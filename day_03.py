# Input
import re

input = open('data/day_03.txt').read()

# Part 1
print('Part 1')
print(sum([i[0]*i[1] for i in list(map(lambda li: [*map(int, li)], re.findall(r'mul\((\d+),(\d+)\)', input)))]))

# Part 2
print('Part 2')
do_mul = True
total = 0

for line in re.findall(r"(do\(\))|(don't\(\))|(mul)\((\d+),(\d+)\)", input):
    if line[0] == 'do()':
        do_mul = True
    if line[1] == "don't()":
        do_mul = False
    if "mul" in line[2] and do_mul:
        total += int(line[3]) * int(line[4])

print(total)

