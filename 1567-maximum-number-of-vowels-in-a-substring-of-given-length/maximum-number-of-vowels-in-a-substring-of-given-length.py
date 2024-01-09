class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a','e','i','o','u'}
        l,result,count = 0,0,0
        for i in range(len(s)):
            if s[i] in vowel:
                count += 1
            if i-l+1 > k:
                if s[l] in vowel:
                     count -= 1
                l += 1
            result = max(result,count)
        return result
                
        