class Solution(object):
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        def rob_linear(arr):
            prev1, prev2 = 0, 0
            for num in arr:
                temp = prev1
                prev1 = max(prev1, prev2+num)
                prev2 = temp

            return prev1

        return max(
            rob_linear(nums[:-1]),
            rob_linear(nums[1:])
        )