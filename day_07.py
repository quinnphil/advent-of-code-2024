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

import itertools

def solve(equations, part_n_operators):
    solved = []
    for equation in equations:
        operations = list(itertools.product(part_n_operators, repeat=len(equation[1])-1))
        for opers in operations:
            result = equation[1][0]
            for i in range(len(equation[1])-1):
                result = opers[i](result, equation[1][i+1])
                if result > equation[0]:
                    break # on overshoot
            if result == equation[0]:
                solved.append(equation[0])
                break

    return(solved)

equations = get_equations(input)

print("Part 1")
print(sum(solve(equations, [add, mult])))

print("Part 2")
print(sum(solve(equations, [add, mult, combine])))
