class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        r,c,l = len(maze) - 1,len(maze[0])-1, 1
        q = deque([(entrance[0] , entrance[1])])
        maze[entrance[0]][entrance[1]] = "+"

        while q:
            for _ in range(len(q)):
                r1,c1 = q.popleft()
                for (x,y) in ((0,-1),(-1,0),(0,1),(1,0)):
                    r2,c2 = r1+x,c1+y
                    if r2<0 or r2>r or c2<0 or c2>c or maze[r2][c2] == "+":
                        continue
                    if r2 == 0 or r2 == r or c2 == 0 or c2 == c:
                        return l
                    maze[r2][c2] = "+"
                    q.append((r2,c2))
            l += 1
        return -1
        