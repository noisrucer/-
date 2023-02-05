nums = [-100,-98,-1,2,3,4]


start = 0
cur_product = 1
max_product = float('-inf')

for end, val in enumerate(nums):
    if val == 0:
        if len(nums) - end > 3:
            start = end + 1
            cur_product = 1
            continue
        else:
            cur_product *= val
            max_product = max(max_product, cur_product)
            break
    else:
        cur_product *= val
    
    if end - start + 1 == 3:
        max_product = max(max_product, cur_product)
        print(max_product)
        cur_product //= nums[start]

        start += 1

print(max_product)