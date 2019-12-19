#Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices: return 0

        low = 99999
        maxprofit = 0
        
        for price in prices:
            if price <= low:
                low = price
            #price > low
            else:
                if (price - low) > maxprofit:
                    maxprofit = price - low
        
        return maxprofit
