class Solution:
    def makeFancyString(self, s: str) -> str:
        res, i, n = '', 0, len(s)
        while i<n:
            start = i
            while i<n-1 and s[i]==s[i+1]:
                i+=1
            temp_s = s[start:min(start+2, i+1)]
            res += temp_s
            i+=1
        return res