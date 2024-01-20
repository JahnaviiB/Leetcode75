class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        k1 = sorted(c1.keys())
        k2 = sorted(c2.keys())

        v1 = sorted(c1.values())
        v2 = sorted(c2.values())
        
        return k1 == k2 and v1 == v2