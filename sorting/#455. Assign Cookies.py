'''
TC: O(nlogn)
SC: O(1)
'''

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        g, s = sorted(g), sorted(s)
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                res += 1
                i += 1
                j += 1
            else:
                j += 1


        return res