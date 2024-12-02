# Input
right, left = list(map(sorted,(zip(*map(lambda li: map(int, li), [l for l in [line.split() for line in open('data/day_01.txt').readlines()]])))))

print('Part 1')
print(sum(map(lambda a, b: abs(a-b), right, left)))

print('Part 2')
map_n2 = dict(map(lambda e: (e, list(left).count(e)), left))
print(sum(map(lambda a, b: a*map_n2.get(a, 0), right, left)))

