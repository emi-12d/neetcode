from typing import List

# 自分の回答
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                c =  prices[j] - prices[i]
                if diff < c:
                    diff = c
        return diff

# neetcodeの回答
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP


print(Solution().maxProfit(prices = [10,1,5,6,7,1]))
