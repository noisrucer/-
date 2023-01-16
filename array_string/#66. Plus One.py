class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for idx in reversed(range(len(digits))):
            if digits[idx] != 9:
                digits[idx] += 1
                break
            else:
                digits[idx] = 0
        
        if digits[0] == 0:
            digits.insert(0, 1)
        
        return digits