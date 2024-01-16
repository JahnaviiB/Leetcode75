class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zero_count = 0
        win_len = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1
            win_len = max(win_len,i-l+1)
        return win_len
        