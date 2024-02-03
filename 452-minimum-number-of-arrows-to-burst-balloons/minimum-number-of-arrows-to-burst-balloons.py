class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points = sorted(points, key = lambda i: i[1])
        count = -float('inf')
        result = 0

        for j in range(0,n):
            if count < points[j][0]:
                result += 1
                count = points[j][1]
        return result
        