class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        new_nums = [0 for i in range(len(nums))]
        for i in range(1, len(nums)):
            if (nums[i-1]+nums[i])%2==0:
                new_nums[i] = new_nums[i-1]+1
            else:
                new_nums[i] = new_nums[i-1]
        return [new_nums[s]==new_nums[e] for s,e in queries]