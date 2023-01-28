class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = dict()

        for idx, val in enumerate(nums):
            if val in freq:
                if idx - freq[val] <= k:
                    return True
            freq[val] = idx

        return False