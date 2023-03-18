from typing import List


# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:

        # have two variables to track before and before_last items
        current = 0
        previous = 0

        if len(nums) >= 1:
            previous = nums[0]

        if len(nums) > 1:
            current = max(nums[0], nums[1])

        # initially set the max profit as the maximum of previous and current
        max_profit = max(previous, current)
        for i in range(2, len(nums)):
                # for each consecutive iteration, select the maximum possible profit
                max_profit = max((nums[i] + previous), current)

                # set current as previous to move one step further
                previous = current
                # calculated max_profit will be the new current point of the dp array
                current = max_profit

        return max_profit
