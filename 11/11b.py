from functools import cache
import timeit


@cache
def blink(stone, times):
    if times == 0:
        return 1
    times -= 1

    if stone == 0:
        return blink(1, times)
    if len(str(stone)) % 2 == 0:
        left = int(str(stone)[:int(len(str(stone)) / 2)])
        right = int(str(stone)[int(len(str(stone)) / 2):])
        return blink(left, times) + blink(right, times)
    return blink(stone * 2024, times)


def part1():
    print("Part 1:", sum([blink(int(stone), 25) for stone in open("big.txt").read().strip().split()]))


def part2():
    print("Part 2:", sum([blink(int(stone), 75) for stone in open("big.txt").read().strip().split()]))


print("Part 1 runtime:", timeit.timeit("part1()", "from __main__ import part1", number=1) * 1000, "ms")
print("Part 2 runtime:", timeit.timeit("part2()", "from __main__ import part2", number=1) * 1000, "ms")
