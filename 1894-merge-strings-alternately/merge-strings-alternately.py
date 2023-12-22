class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        w3 = ""
        while(i < len(word1) or i < len(word2)):
            if(i < len(word1)):
                w3 += word1[i]
            if(i < len(word2)):
                w3 += word2[i]
            i += 1
        return w3