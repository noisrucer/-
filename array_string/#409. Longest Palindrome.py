class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = defaultdict(int)

        res = 0
        temp = 0

        for char in s:
            freq[char] += 1

        for val in freq.values():
            if val % 2 == 1:
                res += val - 1
                temp = 1
            else:
                res += val
        
        return res + temp