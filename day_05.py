from functools import cmp_to_key

input = open('data/day_05.txt').read().strip()

def get_rules_and_manual_updates(input):

    rules = {}
    updates = []
    rules_raw, updates_raw = input.split('\n\n')

    for line in rules_raw.split():
        p1, p2 = line.split('|')
        if not rules.get(int(p1)):
            rules[int(p1)] = set()
        rules[int(p1)].add(int(p2))

    for line in updates_raw.split('\n'):
        updates.append([*map(int, line.split(','))])

    return rules, updates


def is_vaild_update(update):
    valid_update = True
    rules_after = set()
    for i, page in enumerate(update):
        rules_after = rules.get(page, set())

        if len(set(update[:i]).intersection(rules_after)) >= 1:
            valid_update = False

    if valid_update:
        return True
    else:
        return False


def score(update):
    return sum([u[len(u) // 2] for u in update])

# Process
rules, updates = get_rules_and_manual_updates(input)
updates_good = []
updates_bad = []

for update in updates:
    if is_vaild_update(update):
        updates_good.append(update)
    else:
        updates_bad.append(update)


print("Part 1")
print(score(updates_good))

print("Part 2")
print(score(map(lambda u: sorted(u, key=cmp_to_key(lambda a, b: 1 if b in rules[a] else -1)), updates_bad)))