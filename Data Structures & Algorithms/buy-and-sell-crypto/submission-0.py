class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        buy = prices[0]
        max_profit = 0


        for sell in range(1, len(prices)):
            profit = prices[sell]-buy

            if profit>max_profit:
                max_profit=profit

            if prices[sell]<buy:
                buy = prices[sell]

        return max_profit