class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for e in operations:
            if e == "C":
                res.pop()
            elif e == "D":
                res.append(res[-1] * 2)
            elif e == "+":
                res.append(res[-1] + res[-2])
            else:
                res.append(int(e))

        return sum(res)