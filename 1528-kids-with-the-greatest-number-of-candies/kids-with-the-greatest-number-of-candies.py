class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        j = max(candies)
        result = []
        for i in range(len(candies)):
            total = candies[i] + extraCandies
            result.append(total >= j)
        return result

        


