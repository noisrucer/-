class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = dict()

        for idx, val in enumerate(nums):
            if val in mapping:
                if idx - mapping[val] <= k:
                    return True
            mapping[val] = idx

        return False