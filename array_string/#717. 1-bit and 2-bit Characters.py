class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        res = True

        i = 0

        while i < len(bits):
            if bits[i] == 1:
                i += 2
                res = False
            else:
                i += 1
                res = True

        return res 