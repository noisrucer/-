'''
TC: O(n)
SC: O(n)
'''
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        res = 0
        freq = defaultdict(int)
        for e in nums:
            freq[e] += 1
            if freq[e] == 2:
                res += e
                freq[e] -= 2

        temp = None
        for i in range(-10000, 10001):
            if freq[i] > 0:
                if temp is not None: # be careful of 0 is False!
                    res += temp
                    temp = None
                else:
                    temp = i

        return res
        

'''
TC: O(nlogn)
SC: O(1)
'''
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        res = 0
        for i in range(0, len(nums), 2):
            res += nums[i]
        return res
    
