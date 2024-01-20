class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        not_n1 = []
        not_n2 = []

        for i in nums1:
            if i not in nums2 and i not in not_n2:
                not_n2.append(i)
        
        for i in nums2:
            if i not in nums1 and i not in not_n1:
                not_n1.append(i)

        return [not_n2, not_n1]
        