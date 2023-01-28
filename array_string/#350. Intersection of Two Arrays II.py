class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = dict()

        res = []

        for num in nums2:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for num in nums1:
            if num in freq and freq[num] > 0:
                freq[num] -= 1
                res.append(num)
        
        return res