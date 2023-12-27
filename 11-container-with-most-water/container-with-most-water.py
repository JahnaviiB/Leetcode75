class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        m_a = 0
        while l < r:
            area = (r-l) * min(height[l],height[r])
            m_a = max(m_a,area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return m_a
        