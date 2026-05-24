class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal, maxValue = 99999999, 0
        profit = 0

        for price in prices: 
            if price < minVal: 
                minVal = price 

            newProfit = price - minVal
            if newProfit > profit: 
                profit = newProfit
            

        
        if profit == 0: 
            return 0 
        else: 
            return profit