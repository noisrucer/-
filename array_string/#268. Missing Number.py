class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        for i in range(0, n):
            res += i+1
            res -= nums[i]
        
        return res