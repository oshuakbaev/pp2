nums = input().split()
cnt = 0
i, j = 0, 0
while i < len(nums) - 1:
    j = i
    while j <= len(nums) - 1:
        if nums[i] == nums[j] and i < j:
            cnt += 1
        j += 1
    i += 1
print(cnt)