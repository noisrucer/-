'''
TC: O(n)
SC: O(1)
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        roman2int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}
        n = len(s)
        res = 0
        for i in range(0, n - 1):
            if roman2int[s[i]] >= roman2int[s[i + 1]]:
                res += roman2int[s[i]]
            else:
                res -= roman2int[s[i]]

        res += roman2int[s[n - 1]]
        return res