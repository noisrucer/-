class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        hash_table = dict()
        res = []
        
        for num in nums:
          hash_table[num] = 1
        
        for num in range(1, len(nums) + 1):
          if num not in hash_table:
            res.append(num)
        
        return res
      

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        res = []

        for e in nums:
            e = abs(e)
            nums[e - 1] = -1 * abs(nums[e - 1])
        
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res