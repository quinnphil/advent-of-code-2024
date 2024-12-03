# Input
reports =  [*map(lambda li: [*map(int, li)], [l for l in [line.split() for line in open('data/day_02.txt').readlines()]])]

def get_is_safe(report):
    return (all(0<x-y<4 for x,y in zip(report, report[1:]))) or all(0<y-x<4 for x,y in zip(report, report[1:]))


def get_is_safe_with_problem_dampener(report):
    if get_is_safe(report):
        return True
    return any(get_is_safe(report[:i] + report[i + 1 :]) for i in range(len(report)))

print("Part 1")
print(sum([get_is_safe(r) for r in reports]))

print("Part 2")
print(sum([get_is_safe_with_problem_dampener(r) for r in reports] ))
