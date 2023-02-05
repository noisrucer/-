class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = dict()

        if not ransomNote or not magazine:
            return False

        for i in range(len(magazine)):
            if magazine[i] in freq:
                freq[magazine[i]] += 1
            else:
                freq[magazine[i]] = 1

        for char in ransomNote:
            if char in freq and freq[char] > 0:
                freq[char] -= 1
            else:
                return False

        return True