class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_table = defaultdict(int)
        res = []
        
        for num in set(nums1):
            hash_table[num] += 1

        for num in nums2:
            if num in hash_table and hash_table[num] > 0:
                hash_table[num] -= 1
                res.append(num)

        return res