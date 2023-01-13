'''
TC: O(n)
SC: O(n)
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        target_freq = n // 2
        freq = defaultdict(int)
        for e in nums:
            freq[e] += 1
            if freq[e] > target_freq:
                return e

        return None # guaranteed answer exists