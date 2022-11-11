# 121.
# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
def maxProfit(self, prices: List[int]) -> int:
    maxProfit = 0

    left = 0
    right = 0
    while right < len(prices):

        if prices[left] < prices[right]:
            # while left is less than right we can calculate until we reach right
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
        else:
            left = right
        right += 1
    return maxProfit