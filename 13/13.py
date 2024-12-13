import re

def solve(ax, ay, bx, by, px, py):
    aligned_x = ax * by - ay * bx
    aligned_result = px * by - py * bx

    a = aligned_result / aligned_x

    leftover_x = px - ax * a
    b = leftover_x / bx
    return a, b

groups = [[re.sub('[^0-9\s]', '', section).strip().split() for section in group.split("\n")] for group in open("big.txt").read().split("\n\n")]
tokens_a = 0
tokens_b = 0
for group in groups:
    ax, ay = int(group[0][0]), int(group[0][1])
    bx, by = int(group[1][0]), int(group[1][1])
    px1, py1 = (int(group[2][0]), int(group[2][1]))
    px2, py2 = (int(group[2][0]) + 10_000_000_000_000, int(group[2][1]) + 10_000_000_000_000)
    a1, b1 = solve(ax, ay, bx, by, px1, py1)
    a2, b2 = solve(ax, ay, bx, by, px2, py2)
    if int(a1) == a1 and int(b1) == b1:
        tokens_a += int(a1*3 + b1)
    if int(a2) == a2 and int(b2) == b2:
        tokens_b += int(a2*3 + b2)

print(f"Part 1: {tokens_a}")
print(f"Part 2: {tokens_b}")
