from functools import cache
input = """125 17"""
input = open("data/day_11.txt").read().strip()



@cache
def process_stone(stone, blink, max_blinks):
    if blink == max_blinks:
        return 1

    stone_str = str(stone)
    stone_len = len(stone_str)

    if stone == 0:
        return process_stone(1, blink + 1, max_blinks)
    elif stone_len % 2 == 0:
        return process_stone(int(stone_str[:stone_len//2]), blink + 1, max_blinks) + process_stone(int(stone_str[stone_len//2:]), blink + 1, max_blinks)
    else:
        return process_stone(stone * 2024, blink + 1, max_blinks)


stones = [int(i) for i in input.split(' ')]

print("Part 1")
print( sum(process_stone(stone, 0,max_blinks=25) for stone in stones))

print("Part 2")
print( sum(process_stone(stone, 0, max_blinks=75) for stone in stones))

