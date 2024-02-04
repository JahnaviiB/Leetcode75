class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)

        def isEnough(count):
            return sum(ceil(i/count) for i in piles) <= h

        while l<r:
            mid = (l+r)//2
            if isEnough(mid):
                r = mid
            else:
                l = mid + 1
        return l