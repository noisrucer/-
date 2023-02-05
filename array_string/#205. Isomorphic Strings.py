class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_hash_table = dict()
        t_hash_table = dict()

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] in s_hash_table:
                    if s_hash_table[s[i]] != t[i]:
                        return False
            else:
                s_hash_table[s[i]] = t[i]
                
            if t[i] in t_hash_table:
                if t_hash_table[t[i]] != s[i]:
                    return False
            else:
                t_hash_table[t[i]] = s[i]

        return True
    


