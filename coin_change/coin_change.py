from typing import List


# Time Complexity: O(amount x n)
# Space Complexity: O(n)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # fill a previous array (with 'amount no. of columns') with infinity
        prev = [float("inf") for _ in range(amount + 1)]
        prev[0] = 0 # when I don't have to form a target, I don't need any coins

        for n in coins: # each coin
            curr = [0 for _ in range(amount + 1)] # create the currently processing array
            for i in range(1, len(curr)):
                # carry forward the previous value if current target is less than the coin I have rn
                # else find minimum between denominations-step-back + 1 and previous
                curr[i] = prev[i] if i < n else min(1 + curr[i - n], prev[i])
            prev = curr

        return -1 if curr[-1] == float("inf") else curr[-1]
