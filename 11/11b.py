from functools import cache


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


print(sum([blink(int(stone), 75) for stone in open("big.txt").read().strip().split()]))
