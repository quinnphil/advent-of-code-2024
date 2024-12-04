def get_word_grid(data):
    word_grid = dict()
    for y, row in enumerate(data.split('\n')):
        for x, c in enumerate(row):
            word_grid[(x, y)] = c
    return word_grid

def get_word_coordinates(x, y, word_len=4):
    word_directions = []
    for i in [-1,0,1]:
        for j in [-1, 0, 1]:
            if i == j == 0:
                continue
            word_directions.append([(x+i*k, y+j*k) for k in range(word_len)])
    return word_directions

def get_word_from_coordinates(coords):
    return ''.join([word_grid.get(coord, '') for coord in coords])

def get_x_mas_word_coordinates(x, y):
    return(
        [(x - 1, y + 1), (x, y), (x + 1, y - 1)],
        [(x + 1, y + 1), (x, y), (x - 1, y - 1)],
        [(x + 1, y - 1), (x, y), (x - 1, y + 1)],
        [(x - 1, y - 1), (x, y), (x + 1, y + 1) ]
    )

# Find X's
# Part 1
def part_1(find_word):
    word_count = 0
    for start_letter in [l for l in word_grid if word_grid[l] == find_word[0]]:
        for word_coordinate in get_word_coordinates(*start_letter, word_len=len(find_word)):
            if find_word == get_word_from_coordinates(word_coordinate):
                word_count += 1
    return word_count

# Part 2
def part_2():
    total = 0
    for start_letter in [letter for letter in word_grid if word_grid[letter] == "A"]:
        x_mas_word_coordinates = get_x_mas_word_coordinates(*start_letter)
        words = []
        for word_coordinate in x_mas_word_coordinates:
            words.append(get_word_from_coordinates(word_coordinate))
        if words.count('MAS') == 2:
            total += 1
    return total

input = open('data/day_04.txt').read()
word_grid =get_word_grid(input)

print("Part 1")
print(part_1("XMAS"))
print("Part 2")
print(part_2())






