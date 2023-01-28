class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_table = dict()

        res = []

        for i in range(len(nums2)):
            hash_table[nums2[i]] = i


        i = 0
        j = 0
        count = 1
            
        while i < len(nums1):
            j = hash_table[nums1[i]]
            
            if j + count > len(nums2) - 1:
                res.append(-1)
                count = 1
                i += 1     
            elif nums2[j] < nums2[j + count]:
                res.append(nums2[j + count])
                count = 1
                i += 1
            else:
                count += 1
                if count > len(nums2):
                    res.append(-1)
                    count = 1
                    i += 1

        return res