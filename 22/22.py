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


with open("big.txt", "r") as f:
    evolutions = [evolve(int(line), 2000) for line in f.readlines()]


print(f"Part 1: {sum([e[2000] for e in evolutions])}")
sequences = {}
[changes(evolution_no, evo[i:i+5], sequences) for evolution_no, evo in enumerate(evolutions) for i in range(len(evo) - 4)]
print(f"Part 2: {max([sum(seq.values()) for seq in sequences.values()])}")