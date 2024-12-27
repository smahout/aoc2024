import timeit
from math import floor


def evolve(secret: int, times):
    steps = [secret]
    while len(steps) <= times:
        secret ^= secret * 64
        secret %= 16777216
        secret ^= floor(secret / 32)
        secret %= 16777216
        secret ^= secret * 2048
        secret %= 16777216
        steps.append(secret)
    return steps


# Needs a list of 5
def changes(evolution_no: int, subset: list, sequences: dict):
    sequence = subset[1] % 10 - subset[0] % 10, \
               subset[2] % 10 - subset[1] % 10, \
               subset[3] % 10 - subset[2] % 10, \
               subset[4] % 10 - subset[3] % 10
    if sequence not in sequences:
        sequences[sequence] = {}
    if evolution_no not in sequences[sequence]:
        sequences[sequence][evolution_no] = subset[4] % 10


def part1(evolutions):
    for i, secret in enumerate(evolutions):
        evolutions[i] = evolve(secret, 2000)
    print(f"Part 1: {sum([e[2000] for e in evolutions])}")


def part2(evolutions):
    sequences = {}
    [changes(evolution_no, evo[i:i + 5], sequences) for evolution_no, evo in enumerate(evolutions) for i in range(len(evo) - 4)]
    print(f"Part 2: {max([sum(seq.values()) for seq in sequences.values()])}")


with open("big.txt", "r") as f:
    evolutions = [int(line) for line in f.readlines()]
print(f"Part 1 execution time: {timeit.timeit(lambda: part1(evolutions), number=1)}s")
print(f"Part 2 execution time: {timeit.timeit(lambda: part2(evolutions), number=1)}s")
