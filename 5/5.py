from math import floor


def make_rule(rules, rule):
    subject, after = rule
    if rules.get(subject) is None:
        rules[subject] = []
    rules[subject].append(after)


def check_index_in_update(update, index, rules):
    # Check before
    current = update[index]
    if current in rules:
        for i in range(0, index):
            if update[i] in rules[current]:
                return False
    return True


def order_correctly(values, update, rules):
    for v in values:
        can_go_before = True
        for v2 in values:
            if v2 in rules and v in rules[v2]:
                can_go_before = False
        if can_go_before:
            update.append(v)
            values.remove(v)
            if len(values) > 0:
                return order_correctly(values, update, rules)
    return update


rules = {}
with open("big5.txt") as f:
    in_rules, updates = f.read().split("\n\n")

in_rules = [rule.strip().split("|") for rule in in_rules.split("\n")]
updates = [update.strip().split(",") for update in updates.split("\n")]

for rule in in_rules:
    make_rule(rules, rule)

good_updates = []
bad_updates = []
for update in updates:
    still_correct = True
    for n in range(len(update)):
        if not check_index_in_update(update, n, rules):
            still_correct = False
            break
    if still_correct:
        good_updates.append(update)
    else:
        bad_updates.append(update)

new_good_updates = []
for update in bad_updates:
    new_good_updates.append(order_correctly(update, [], rules))

print("Part1: ", sum([int(u[floor(len(u) / 2)]) for u in good_updates]))
print("Part2: ", sum([int(u[floor(len(u) / 2)]) for u in new_good_updates]))
