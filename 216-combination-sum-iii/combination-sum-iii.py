class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        for i in combinations(range(1,10),k):
            if sum(i) == n:
                result.append(i)
        return result
        