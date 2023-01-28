# hash_table version 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()

        for idx in range(len(nums)):
            if target - nums[idx] in hash_table:
                return [hash_table[target - nums[idx]], idx]
            else:
                hash_table[nums[idx]] = idx
        
        return None
    

# hash_table version 2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()

        for idx, val in enumerate(nums):
            if target - val in hash_table:
                return [hash_table[target - val], idx]
            hash_table[val] = idx
        
        return None