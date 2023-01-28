class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 정규표현식 + 슬라이싱
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]

        # 리스트
        """
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        
        return True
        """

        # reversed
        """
        strs = []

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        s_reversed = list(reversed(strs))

        return strs == s_reversed
        """