nums = [1,3,3,5,4,7]

res = 0
count = 1

for i in range(len(nums) - 1):
    if nums[i] < nums[i + 1]:
        count += 1
        res = max(res, count)
    elif nums[i] > nums[i + 1]:
        count = 1
        
print(res)