class Solution:
    def isValid(self, s: str) -> bool:
        hash_table = {")": "(", "]": "[", "}": "{"}

        stack = []

        for bracket in s:
            if bracket in hash_table:
                if not stack:
                    return False
                if stack[-1] == hash_table[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)

        return not stack