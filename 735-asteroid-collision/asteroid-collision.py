class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for i in asteroids:
            while result and i < 0 < result[-1]:
                if -i > result[-1]:
                    result.pop()
                    continue
                elif -i == result[-1]:
                    result.pop()
                break
            else:
                result.append(i)
        return result

        