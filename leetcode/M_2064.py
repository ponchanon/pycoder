class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        mini, maxi = 1, max(quantities)
        while mini < maxi:
            mid = (mini + maxi) // 2
            if sum(ceil(q / mid) - 1 for q in quantities) <= n:
                maxi = mid
            else:
                mini = mid + 1
        return maxi