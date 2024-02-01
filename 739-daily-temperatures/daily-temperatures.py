class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = [] #empty stack
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while s and temperatures[i] > temperatures[s[-1]]:
                j = s.pop()
                result[j] = i - j
            s.append(i)
        return result
        