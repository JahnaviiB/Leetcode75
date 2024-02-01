class SmallestInfiniteSet:

    def __init__(self):
        self.i = 1
        self.j = set()
        

    def popSmallest(self) -> int:
        if self.j:
            result = min(self.j)
            self.j.remove(result)
            return result
        else:
            self.i += 1
            return self.i - 1
        

    def addBack(self, num: int) -> None:
        if self.i > num:
            self.j.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)