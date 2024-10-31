class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resList = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            resList[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1,-1):
            resList[i] *= postfix
            postfix *= nums[i]
        return resList