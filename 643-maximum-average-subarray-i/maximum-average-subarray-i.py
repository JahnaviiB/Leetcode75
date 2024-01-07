class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current = max_sum = sum(nums[:k])
        for i in range(k,len(nums)):
            current += nums[i] - nums[i-k]
            max_sum = max(max_sum,current)
        return max_sum/k
        