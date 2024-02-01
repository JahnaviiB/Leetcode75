class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        result = 0
        count = 0
        heap = []

        merge = [(nums2[i], nums1[i]) for i in range(len(nums1))]
        merge.sort(reverse = True)

        for i,j in merge:
            if len(heap) == k:
                count -= heapq.heappop(heap)
            
            count += j
            heapq.heappush(heap,j)

            if len(heap) == k:
                result = max(result, count * i)
        return result


        