class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] *(n+1)
        dp[1] = nums[0]
        for i in range(1,n):
            dp[i+1] = max(dp[i-1] + nums[i], dp[i])
        return dp[n]
        