import re

# Input
input = open('data/day_03.txt').read()

# Part 1
print('Part 1')
print(sum(int(a) * int(b) for a, b in re.findall(r'mul\((\d+),(\d+)\)', input)))

# Part 2
print('Part 2')
do_mul = True
total = 0

for m in (re.finditer(r"(do\(\))|(don't\(\))|(mul)\((?P<a>\d+),(?P<b>\d+)\)", input)):
    if m.group(0) =='do()':
        do_mul = True
    elif m.group(0) =="don't()":
        do_mul = False
    else:
        total = total + (int(m.group('a')) * int(m.group('b')) * do_mul)

print(total)

