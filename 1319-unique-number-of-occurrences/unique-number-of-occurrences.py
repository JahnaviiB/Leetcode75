class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hmap = {}
        for i in arr:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 1
        
        count = set()
        for j in hmap:
            if hmap[j] in count:
                return False
            count.add(hmap[j])
        
        return True
        