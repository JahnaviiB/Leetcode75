class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = [1]*n
        for i in range(m-1):
            nextrow = [1]*n
            for j in range(n-2,-1,-1):
                nextrow[j] = nextrow[j+1] + result[j]
            result = nextrow

        return result[0]

        