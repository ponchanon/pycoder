class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)

        # Avoid modifying the input directly
        # Create a copy of the input array
        values = nums.copy()

        for i in range(n):
            for j in range(n - i - 1):
                if values[j] <= values[j + 1]:
                    # No swap needed
                    continue
                else:
                    if bin(values[j]).count("1") == bin(values[j + 1]).count(
                        "1"
                    ):
                        # Swap the elements
                        values[j], values[j + 1] = values[j + 1], values[j]
                    else:
                        return False
        return True
        


# class Solution:
#     def canSortArray(self, nums: List[int]) -> bool:
#         prev_max = float('-inf')
#         curr_min, curr_max = nums[0], nums[0]
#         curr_bits = nums[0].bit_count()
#         for i in range(len(nums)):
#             if nums[i].bit_count()!=curr_bits:
#                 if prev_max > curr_min:
#                     return False
#                 prev_max = curr_max
#                 curr_bits = nums[i]
#                 curr_min, curr_max = nums[i], nums[i]
#             else:
#                 curr_min = min(curr_min, nums[i])
#                 curr_max = max(curr_max, nums[i])
#         return curr_min >= prev_max