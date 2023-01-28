# First Try
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dct = defaultdict(int)

        for num in nums:
            dct[num] += 1
        
        for item in dct.items():
            if item[1] == 1:
                return item[0]
            
# Second Try
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]

        for i in range(1, len(nums)):
            res ^= nums[i]

        return res 