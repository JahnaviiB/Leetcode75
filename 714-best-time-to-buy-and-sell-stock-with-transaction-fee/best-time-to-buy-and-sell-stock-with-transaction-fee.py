class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        bp = -prices[0]
        sp = 0
        for i in prices[1:]:
            bp = max(bp, sp-i)
            sp = max(sp, i-fee+bp)
        return sp


        