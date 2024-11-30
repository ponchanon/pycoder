class Solution:
    def isHappy(self, n: int) -> bool:
        cache = {}
        while (n!=1) and (n not in cache):
            total = 0
            for d in str(n):
                total += int(d) ** 2
            cache[n] = total
            n = total
        return n==1