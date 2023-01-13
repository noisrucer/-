class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num = nums[0]
        count = 1

        while len(set(nums)) != len(nums):
            if num == nums[count]:
                nums.pop(count)
            else:
                count += 1
                num = nums[count - 1]

        return len(nums)