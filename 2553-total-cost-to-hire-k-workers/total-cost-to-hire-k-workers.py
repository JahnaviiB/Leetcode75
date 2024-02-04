class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        i, j =0, n-1
        p1 = []
        p2 = []
        result =0

        while k>0:
            while len(p1) < candidates and i <= j:
                heapq.heappush(p1,costs[i])
                i += 1
            while len(p2) < candidates and i<= j:
                heapq.heappush(p2, costs[j])
                j -= 1

            j1 = p1[0] if p1 else float('inf')
            j2 = p2[0] if p2 else float('inf')

            if j1 <= j2:
                result  += j1
                heapq.heappop(p1)
            else:
                result += j2
                heapq.heappop(p2)
            
            k -= 1
        return result


        