import copy

input = open('data/day_07.txt').read().strip('\n')

def get_equations(data):
    equations = []
    for line in data.split('\n'):
        t, vs = line.split(':')
        equations.append([int(t), [int(v) for v in vs.split()]])

    return equations

def add(a, b):
    return a + b

def mult(a, b):
    return a * b

def combine(a, b):
    return (a * 10**(len(str(b))) + b)


def solve(equation, operators):
    target = equation[0]
    a = equation[1].pop(0)
    b = equation[1].pop(0)

    have_solution = False
    for operator in operators:
        total = operator(a, b)

        # Done?
        if total == target and len(equation[1]) == 0:
            have_solution = True
        elif (a > target) or len(equation[1]) == 0: # overshoot or nowhere to go
            have_solution = False
        elif len(equation[1]) > 0:
            have_solution = solve([target, [total] + equation[1]], operators)
        else:
            have_solution = False

        if have_solution:
            break

    return have_solution

equations = get_equations(input)
print("Part 1")
print(sum([e[0] for e in equations if solve(copy.deepcopy(e), [add, mult])]))

print("Part 2")
print(sum([e[0] for e in equations if solve(copy.deepcopy(e), [add, mult, combine])]))
