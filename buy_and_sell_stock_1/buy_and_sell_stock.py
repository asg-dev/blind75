from typing import List


# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0

        while r < len(prices):
            # keep track of maxProfit at each iteration if we see a rise in stock price
            if prices[r] > prices[l]:
                maxProfit = max(maxProfit, (prices[r] - prices[l]))
            else: # move l to r to ignore or skip
                l = r
            r += 1
        return maxProfit
