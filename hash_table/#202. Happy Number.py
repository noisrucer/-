class Solution:
    def isHappy(self, n: int) -> bool:
        hash_set = set()
        hash_set.add(n)

        while n != 1:
            temp = 0
            while n > 0:
                remainder = n % 10
                n //= 10
                temp += (remainder ** 2)
            
            if temp in hash_set:
                return False
            
            hash_set.add(temp)
            n = temp

        return True