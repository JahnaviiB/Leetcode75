class Solution:
    def gcdOfStrings(self, s1: str, s2: str) -> str:
        if s1 + s2 != s2 + s1:
            return ""

        i = gcd(len(s1), len(s2))
        return s1[:i]
        