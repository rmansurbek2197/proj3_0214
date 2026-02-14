# 11
n = int(input())
nums = list(map(int, input().split()))
unique = []
for x in nums:
    if x not in unique:
        unique.append(x)
print(*unique)

# 12
n = int(input())
nums = list(map(int, input().split()))
max_sum = nums[0]
current_sum = nums[0]
for i in range(1, n):
    current_sum = max(nums[i], current_sum + nums[i])
    if current_sum > max_sum:
        max_sum = current_sum
print(max_sum)

# 13
n = int(input())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
print(*nums)

# 14
n = int(input())
nums = list(map(int, input().split()))
second = None
first = float('-inf')
for x in nums:
    if x > first:
        second = first
        first = x
    elif x > second and x != first:
        second = x
print(second)

# 15
n = int(input())
nums = list(map(int, input().split()))
target = int(input())
found = False
for i in range(n):
    for j in range(i + 1, n):
        if nums[i] + nums[j] == target:
            print(i, j)
            found = True
            break
    if found:
        break
if not found:
    print(-1)
