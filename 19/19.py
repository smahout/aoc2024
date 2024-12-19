from functools import cache

@cache
def dfs(remainder):
    if remainder == "":
        return 1

    total = 0
    for towel in towels:
        if len(towel) <= len(remainder) and towel == remainder[:len(towel)]:
            total += dfs(remainder[len(towel):])
    return total

with open("big.txt", "r") as f:
    parts = f.read().split('\n\n')
    towels, patterns = (
        set([pattern.strip() for pattern in parts[0].split(',')]),
        [pattern.strip() for pattern in parts[1].split('\n')]
    )

print(sum([dfs(pattern) for pattern in patterns]))