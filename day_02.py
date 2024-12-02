# Input
reports =  list(map(list,(map(lambda li: map(int, li), [l for l in [line.split() for line in open('data/day_02.txt').readlines()]]))))

def get_is_safe(report):
    return (all( report[i] < report[i + 1] and abs(report[i] - report[i + 1]) < 4 for i in range(len(report) - 1) ) or
            all( report[i] > report[i + 1] and abs(report[i] - report[i + 1]) < 4 for i in range(len(report) - 1) ))

def get_is_safe_with_problem_dampener(report):
    if get_is_safe(report):
        return True
    return any(get_is_safe(report[:i] + report[i + 1 :]) for i in range(len(report)))

print("Part 1")
print(sum([get_is_safe(r) for r in reports]))

print("Part 2")
print(sum([get_is_safe_with_problem_dampener(r) for r in reports] ))
