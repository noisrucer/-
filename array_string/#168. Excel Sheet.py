class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        import string
        alphabet = string.ascii_uppercase
        hash_table = dict()

        digits = 26

        res = ""

        for i in range(len(alphabet)):
            hash_table[i + 1] = alphabet[i]
            
        if columnNumber in hash_table:
            return hash_table[columnNumber]


        while columnNumber > digits:    
            remainder = columnNumber % digits
            columnNumber //= digits

            if remainder == 0:
                if columnNumber == 1:
                    break
                else:
                    columnNumber -= 1
                    res += hash_table[digits]
                    break
            
            res += hash_table[remainder]

        res += hash_table[columnNumber]

        return res[::-1]