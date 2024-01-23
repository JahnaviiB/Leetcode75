class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = []
        potions.sort()
        n = len(potions)
        for i in spells:
            l,r = 0,n-1
            index = n
            while l <= r:
                m = (l+r)//2
                if i * potions[m] >= success:
                    r = m-1
                    index = m
                else:
                    l = m+1
            result.append(n-index)
        return result
        