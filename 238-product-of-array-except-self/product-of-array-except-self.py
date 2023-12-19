class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left = [1]*l
        for i in range(1,l):
            left[i] = left[i-1] * nums[i-1]

        right = nums[-1]
        for i in range(l-2,-1,-1):
            left[i] *= right
            right *= nums[i]
        return left
        