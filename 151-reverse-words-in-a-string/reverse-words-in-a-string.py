class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = words[::-1]
        reversed_string = ' '.join(reversed_words)
        return reversed_string