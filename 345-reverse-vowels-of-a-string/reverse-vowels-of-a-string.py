class Solution:
    def reverseVowels(self, s: str) -> str:
        result = []
        ans = ""
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for each in s:
            if each in vowels:
                result.append(each)
        for i in s:
            if i in vowels:
                ans += result.pop()
            else:
                ans += i
        return ans