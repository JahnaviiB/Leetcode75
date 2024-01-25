class Solution:
    def countBits(self, n: int) -> List[int]:
        c = [0]
        for i in range(1,n+1):
            c.append(c[i >> 1] + i%2)
        return c
        