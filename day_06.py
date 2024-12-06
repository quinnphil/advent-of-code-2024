import copy

input = open('data/day_06.txt').read().strip()

lab = dict()
guard = {
    "position": (-1,-1),
    "direction": (0,0)
}

for y, line in enumerate(input.split('\n')):
    for x, space in enumerate(line):
        if space == "#":
            lab[x,y] = 1
        else:
            lab[x,y] = 0
        if space == "^":
            guard['position'] = (x, y)
            guard['direction'] = (0, -1)

def walk_lab(lab, guard):
    in_lab = True
    path = dict()
    while in_lab:
        # Check if still in lab
        if lab.get(guard['position']) is None:
            # left lab
            in_lab = False
        else:
            # Count position
            if path.get(guard['position']) is None:
                path[guard['position']] = []
            elif guard['direction'] in path[guard['position']]:
                # Loop detected
                return dict()
            path[guard['position']].append(guard['direction'])

            # New position
            is_next_position = False
            while not is_next_position:
                next_position = (guard['position'][0] + guard['direction'][0],
                                 guard['position'][1] + guard['direction'][1])

                if lab.get(next_position) is None:
                    is_next_position = True
                    in_lab = False
                if lab.get(next_position) == 1:
                # Obstacle ahead - adjust guard direction
                    if guard['direction'] == (1, 0):
                        guard['direction'] = (0, 1)
                    elif guard['direction'] == (0, 1):
                        guard['direction'] = (-1, 0)
                    elif guard['direction'] == (-1, 0):
                        guard['direction'] = (0, -1)
                    else:
                        guard['direction'] = (1, 0)
                else:
                    is_next_position = True
                    guard['position'] = next_position

    return path



print("Part 1")
lab_path = walk_lab(lab, copy.copy(guard))
print(len(lab_path))

# Part 2
print("Part 2")
lab_path.pop(guard['position'])
loop_labs = 0
for space in lab_path:
    lab_copy = copy.copy(lab)
    lab_copy[space] = 1
    result = walk_lab(lab_copy, copy.copy(guard))
    if len(result) == 0:
        loop_labs += 1
print(loop_labs)