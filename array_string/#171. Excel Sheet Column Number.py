class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        import string
        alphabet = string.ascii_uppercase
        
        # 알파벳에 대응하는 수 A -> 1
        columnNumber = dict()

        # 자릿수
        digits = 26

        res = 0

        # 딕셔너리 생성
        for i in range(len(alphabet)):
            columnNumber[alphabet[i]] = i + 1

        # 알파벳이 한 개라면 딕셔너리에서 바로 리턴
        if len(columnTitle) == 1:
            return columnNumber[columnTitle[0]]
        
    
        for i in range(len(columnTitle) - 1, -1, -1):
            res += columnNumber[columnTitle[i]] * (digits ** (len(columnTitle) - 1 - i))

        return res
    
    
