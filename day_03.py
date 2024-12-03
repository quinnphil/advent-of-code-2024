import re

# Input
input = open('data/day_03.txt').read()

for p in [1,2]:
    print(f"Part {p}")

    do_mul = True
    total = 0

    for m in (re.finditer(r"(do\(\))|(don't\(\))|(mul)\((?P<a>\d+),(?P<b>\d+)\)", input)):
        if m.group(0) =='do()':
            do_mul = True
        elif m.group(0) =="don't()":
            do_mul = False
        else:
            total += (int(m.group('a')) * int(m.group('b')) * (1 if p==1 else do_mul))

    print(total)

