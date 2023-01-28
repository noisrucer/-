class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, j = 0, 1

        while j < len(nums):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                j += 1