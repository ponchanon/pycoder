class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi, l, r = 0, 0, 1
        
        while r<len(prices):
            if prices[l]>prices[r]:
                l=r
                maxi = max(maxi,prices[r]-prices[l])
                r+=1
            else:
                maxi = max(maxi,prices[r]-prices[l])
                r+=1
            print(maxi)
        return maxi