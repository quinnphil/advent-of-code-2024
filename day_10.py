input = open('data/day_10.txt').read().strip()

from collections import deque

def get_topographic_map(input):
    t_map = dict()
    for y, line in enumerate(input.split('\n')):
        for x, e in enumerate(line):
            if e.isnumeric():
                t_map[x, y] = int(e)
            else:
                t_map[x, y] = -1

    return t_map

def walk_trails(trail_queue, t_map):
    trail_heads = dict()
    while trail_queue:
        pos_c, height, t_path  = trail_queue.popleft()
        for k in [(0, -1), (1, 0), (0, 1), (-1, 0)]:

            next_pos = (pos_c[0] + k[0], pos_c[1] + k[1])
            if next_height := t_map.get(next_pos, None):
                if next_height == height + 1:
                    if next_height == 9:
                        if not trail_heads.get(next_pos):
                            trail_heads[next_pos] = []
                        trail_heads[next_pos].append(t_path)
                    else:
                        trail_queue.append((next_pos, next_height, t_path + [next_pos]))
    return trail_heads

t_map = get_topographic_map(input) # Topographic Map
trail_queue = deque([(t_start, t_map[t_start], [t_start]) for t_start in t_map if t_map[t_start] == 0])


print('Part 1')
trail_heads = walk_trails(trail_queue, t_map)

winning = set()
for th in trail_heads:
    for trail in trail_heads[th]:
        winning.add((th, trail[0]))
print(len(winning))

print('Part 2')
ratings = {}
for th in trail_heads:
    for trail in trail_heads[th]:
        if not ratings.get(trail[0]):
            ratings[trail[0]] = 0
        ratings[trail[0]] += 1

print(sum(ratings.values()))