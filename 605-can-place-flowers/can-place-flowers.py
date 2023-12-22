class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while(i < len(flowerbed)):
            if flowerbed[i] == 0:
                next_plot = flowerbed[i + 1] if i + 1 < len(flowerbed) else 0
                prev_plot = flowerbed[i - 1] if i - 1 >= 0 else 0
                if next_plot == 0 and prev_plot == 0:
                    flowerbed[i] = 1
                    n -= 1
                    i += 2
                else:
                    i += 1
            else:
                i += 2
        return n <= 0