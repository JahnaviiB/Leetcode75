class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        i = 0
        count = 0
        n = len(intervals)
        for j in range(1,n):
            if intervals[i][1] > intervals[j][0]:
                count += 1
            else:
                i = j
        return count