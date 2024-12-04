left, right = [], []
with open("inputs/big1.txt") as f:
    for line in f:
        line = line.replace("\n", "" )
        pair = line.split("   ")
        left.append(int(pair[0]))
        right.append(int(pair[1]))

left = sorted(left)
right = sorted(right)

distance = 0
for i in range(len(left)):
    distance += abs(left[i] - right[i])
print("Distance:", distance)

product_sum = 0
for i in range(len(left)):
    product_sum += right.count(left[i]) * left[i]
print("Product sum:", product_sum)
