class Solution(object):
    def removeElement(self, nums, val):
        r = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[r] = nums[i]
                r += 1
        return r