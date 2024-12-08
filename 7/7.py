from copy import deepcopy
from operator import concat

def math(input, intermediate, result):
    int_mult = 1 if intermediate is None else intermediate
    int_plus = 0 if intermediate is None else intermediate
    concatination = 0
    if len(input) > 0:
        v = input.pop()
        if intermediate is not None:
            if math(deepcopy(input), int(concat(str(intermediate), str(v))), result) == result:
                return result
        if math(deepcopy(input), v * int_mult, result) == result:
            return result
        if math(deepcopy(input), v + int_plus, result) == result:
            return result
    elif intermediate == result:
        return result
    return 0

equations = {int(l.split(":")[0]): list(map(int, l.split(":")[1].split())) for l in open("big7.txt")}
sum = 0
print()
for result in equations:
    sum += math(equations[result][::-1], None, result)
print(sum)