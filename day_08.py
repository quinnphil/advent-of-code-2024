input = open('data/day_08.txt').read().strip()

def get_antennas(input):
    nodes = dict()
    max_x = 0
    max_y = 0
    for y, line in enumerate(input.split('\n')):
        if max_y < y:
            max_y = y
        for x, node in enumerate(line):
            if max_x < len(line):
                max_x = len(line)
            if node != '.':
                if nodes.get(node) is None:
                    nodes[node] = []
                nodes[node].append((x,y))

    return max_x, max_y, nodes

max_x, max_y, antennas = get_antennas(input)
print(f"{max_x=} {max_y=} {antennas=}")

antinodes = set()

def part1():
    for antenna_set in antennas.values():
        for i in range(len(antenna_set)):
            for j in range(len(antenna_set)):
                if i == j: continue
                node_a = antenna_set[i]
                node_b = antenna_set[j]

                delta_x = 2 * node_a[0] - node_b[0]
                delta_y = 2 * node_a[1] - node_b[1]

                antinodes.add((delta_x, delta_y))
    return antinodes

def part2():
    for antenna_set in antennas.values():
        for i in range(len(antenna_set)):
            for j in range(len(antenna_set)):
                if i == j: continue
                node_a = antenna_set[i]
                node_b = antenna_set[j]

                delta_x = node_a[0] - node_b[0]
                delta_y = node_a[1] - node_b[1]

                x = node_a[0]
                y = node_a[1]

                while 0 <= x < max_x and 0 <= y <= max_y:
                    antinodes.add((x, y))
                    x += delta_x
                    y += delta_y

    return antinodes

antinodes = part1()
print(len([a for a in antinodes if 0 <= a[0] < max_x and 0 <= a[1] <= max_y ]))

antinodes = part2()
print(len([a for a in antinodes if 0 <= a[0] < max_x and 0 <= a[1] <= max_y ]))
# print(len(antinodes)) # 597 too low