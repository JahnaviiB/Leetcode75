class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        r = sum(nums)
        for i in range(len(nums)):
            l += nums[i]
            if r == l:
                return i
            r -= nums[i]
        return -1
        