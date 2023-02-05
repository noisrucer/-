'''
1. 일반화
이진 배열이 주어지면 배열에서 연속된 1의 최대 개수를 반환하라.

2. 점화식
f(nums) = 연속된 1의 최대 개수

- Base Case
f(Null) = 0
if f(nums) not in 1 = 0

- General Case
1. nums[i]가 1일 때 count = count + 1을 해준다.
1-1. 만약 i가 len(nums) - 1이라면 바로 max(res, count)을 res에 저장해서 반환해라
2. nums[i]가 0일 때 max(res, count)를 res에 저장하고 count는 0으로 초기화 시켜라


'''

# First try
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = 0

        if not nums:
            return 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if i == len(nums) - 1:
                    return max(res, count)
            else:
                res = max(res, count)
                count = 0
        
        return res
    
# Second try
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum_len, count = 0, 0
        
        for e in nums:
            if e == 1:
                count += 1
                maximum_len = max(maximum_len, count)
            else:
                count = 0

        return maximum_len