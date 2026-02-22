ls = [2, 4, 3, 1, 6, 5, 9, 8, 7, 5]
# output: [(2, 8), (4, 6), (3, 7), (1, 9)]

result = []
used = []
i = 0

while i < len(ls):
    j = i + 1
    while j < len(ls):
        if ls[i] + ls[j] == 10:
            if i not in used and j not in used:
                result.append((ls[i], ls[j]))
                used.append(i)
                used.append(j)
        j += 1
    i += 1
print(result)

nums = [2, 4, 3, 1, 6, 5, 9, 8, 7, 5]
target_sum = 10

result = []

# Check all pairs (i, j) where i < j
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target_sum:
            result.append((nums[i], nums[j]))

print(f"Pairs with sum {target_sum}: {result}")