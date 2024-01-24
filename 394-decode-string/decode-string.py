class Solution:
    def decodeString(self, s: str) -> str:
        result = []
        s1 = ""
        count = 0
        for i in s:
            if i.isdigit():
                count = count * 10 + int(i)
            elif i == "[":
                result.append(count)
                result.append(s1)
                count = 0
                s1 = ""
            elif i == "]":
                s2 = result.pop()
                count1 = result.pop()
                s1 = s2 + s1 * count1
            else:
                s1 += i
        return s1



        