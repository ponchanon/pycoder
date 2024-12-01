# Optimized Solution
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        inc = 2*(numRows-1)
        res = []
        for r in range(numRows):
            for c in range(r, len(s), inc):
                res.append(s[c])
                c2 = c+inc-2*r
                if r not in (0,numRows-1) and c2<len(s):
                    res.append(s[c2])
        return ''.join(res)
            
            
