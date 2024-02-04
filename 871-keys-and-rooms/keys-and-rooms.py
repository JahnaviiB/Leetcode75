class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n, keys, result = len(rooms), deque([0]), set()

        while keys and len(result) < n:
            i = keys.popleft()
            result.add(i)

            for j in rooms[i]:
                if j not in result:
                    keys.append(j)
        return len(result) == n
        