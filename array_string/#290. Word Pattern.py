class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = dict()

        s = s.split()

        if len(pattern) != len(s):
            return False
            
        for i in range(len(pattern)):
            if pattern[i] not in mapping.keys():
                if s[i] in mapping.values():
                    return False
                mapping[pattern[i]] = s[i]
            elif mapping[pattern[i]] != s[i]:
                return False
        
        return True