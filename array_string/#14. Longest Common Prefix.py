class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        if not strs:
            return ""

        for word in strs[1:]:
            temp = ""
            for i in range(len(min(prefix, word))):
                if prefix[i] != word[i]:
                    break
                else:
                    temp += word[i]

            prefix = temp
       
        return prefix