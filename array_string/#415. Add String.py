class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len_num1 = len(num1)
        len_num2 = len(num2)

        carry = 0

        res = ""

        if len(num1) == 1 and len(num2) == 1:
            return str((ord(num1[0]) - 48) + (ord(num2[0]) - 48))


        while len_num1 > 0 or len_num2 > 0:
            add_num = carry
            
            if len_num1 > 0:
                add_num += (ord(num1[len_num1 - 1]) - 48)
                
            if len_num2 > 0:
                add_num += (ord(num2[len_num2 - 1]) - 48)
                
            carry = add_num // 10
            
            total_add = add_num % 10
            
            res += str(total_add)
            
            len_num1 -= 1
            len_num2 -= 1
        
        if carry != 0:
            res += str(carry)
            
        return res[::-1]