class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        j = deque(senate)
        while len(j) > 1:
            i = j.popleft()
            try:
                j.remove('R' if i == 'D' else 'D')
                j.append(i)
            except ValueError:
                pass
        return "Dire" if j.pop() == "D" else "Radiant"

        