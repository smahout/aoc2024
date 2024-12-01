left, right = [], []
with open("input.txt") as f:
    for line in f:
        line = line.replace("\n", "" )
        pair = line.split("   ")
        left.append(pair[0])
        right.append(pair[1])

left = sorted(left)
right = sorted(right)

distance = 0
for i in range(len(left)):
    distance += abs(int(left[i]) - int(right[i]))
print("Distance:", distance)

product_sum = 0
for i in range(len(left)):
    product_sum += right.count(left[i]) * int(left[i])
print("Product sum:", product_sum)
