class Solution:
    def findCircleNum(self, g: List[List[int]]) -> int:
        v = [False] * len(g)

        def dfs(i):
            for j in range(len(g)):
                if g[i][j] and not v[j]:
                    v[j] = True
                    dfs(j)

        ans = 0
        for i in range(len(g)):
            if not v[i]:
                dfs(i)
                ans += 1
        return ans