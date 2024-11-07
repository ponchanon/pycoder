class Solution:
    def compressedString(self, word: str) -> str:
        res = ''
        c_val = 1
        for i in range(len(word)-1):
            if word[i]==word[i+1] and c_val < 9:
                c_val +=1
                continue
            else:
                res = res + str(c_val) + word[i]
                c_val=1
        return res + str(c_val) + word[-1]