class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        l,res=0,0
        d=collections.defaultdict(int)
        for i in range(n):
            d[nums[i]]+=1
            while max(d.keys())-min(d.keys())>2:
                print(l)
                d[nums[l]] -= 1
                if d[nums[l]]==0:
                    del d[nums[l]]
                l+=1
            res += i-l+1
        return res