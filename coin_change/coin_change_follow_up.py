from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        dp_grid = []
        prev = [float("inf") for _ in range(amount + 1)]
        prev[0] = 0

        dp_grid.append(prev)

        for n in coins:
            curr = [0 for _ in range(amount + 1)]
            for i in range(1, len(curr)):
                curr[i] = prev[i] if i < n else min(1 + curr[i - n], prev[i])
            dp_grid.append(curr)
            prev = curr

        denominations = self.find_denominations(dp_grid, coins)
        print(denominations)
        # return -1 if curr[-1] == float("inf") else curr[-1]
        return -1 if len(denominations) == 0 else len(denominations)

    def find_denominations(self, grid, coins):
        denominations = []
        row = len(grid) - 1
        column = len(grid[0]) - 1

        while row != 0 and column != 0:
            coin = coins[row - 1]
            if grid[row][column] != grid[row - 1][column]:
                denominations.append(coin)
                column -= coin
            else:
                row -= 1

        return denominations
