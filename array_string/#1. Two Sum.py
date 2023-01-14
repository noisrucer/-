class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num1 = target - nums[i]

            if num1 in nums:
                num2 = nums.index(num1)
                if i != num2:
                    return [i, num2]
                
                