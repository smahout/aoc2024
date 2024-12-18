from re import findall, split
from itertools import chain


def sum_multiply(input):
    return sum([int(n[0]) * int(n[1]) for n in [findall('\d+', m) for m in findall(r'(mul\(\d+,\d+\))', input)]])


with open("big.txt") as f:
    r = f.read()
    print("Part 1:", sum_multiply(r))
    parts = list(chain.from_iterable([split(r"(do\(\))", s) for s in split(r"(don't\(\))", r)]))
    print("Part 2:",
          sum([sum_multiply(parts[i]) if i == 0 or parts[i - 1] != "don't()" else 0 for i in range(len(parts))]))
