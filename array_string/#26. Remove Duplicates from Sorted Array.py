# First Try
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
    
# Second Try
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1

        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return i + 1