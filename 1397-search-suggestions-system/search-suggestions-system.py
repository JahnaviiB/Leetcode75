class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        n = len(searchWord)
        products.sort()
        result = []
        prev = products

        for i in range(n):
            j = []
            for k in prev:
                if len(k) > i and k[i] == searchWord[i]:
                    j.append(k)

            prev = j
            result.append(j[:3])
        return result
        