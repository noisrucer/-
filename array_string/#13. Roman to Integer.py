class Solution:
    def romanToInt(self, s: str) -> int:
        dct = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500,
        "M":1000}

        res = 0

        for c in list(s):
            res += dct[c]

        return res