class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = dict()

        for num in nums:
            if num in freq:
                freq[num] += 1
                if freq[num] > (len(nums) // 2):
                    return num
            else:
                freq[num] = 1
        
        return 1