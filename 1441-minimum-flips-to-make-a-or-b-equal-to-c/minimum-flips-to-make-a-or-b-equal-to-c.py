class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        result = 0
        while a or b or c:
            i,j,k = a%2, b%2, c%2
            print(i,j,k)
            if k == 0:
                result += (i+j)
            elif i == 0 and j == 0:
                result += 1
            a,b,c = a//2, b//2, c//2
        return result
        