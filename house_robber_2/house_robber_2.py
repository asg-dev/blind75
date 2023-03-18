from typing import List


# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def new_rob(self, nums):
        current = 0
        previous = 0

        if len(nums) >= 1:
            previous = nums[0]

        if len(nums) > 1:
            current = max(nums[0], nums[1])

        max_profit = max(previous, current)
        for i in range(2, len(nums)):
                max_profit = max((nums[i] + previous), current)
                previous = current
                current = max_profit

        return max_profit

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        # innately, the solution is simple. If the houses are arranged in a circle, you can't rob
        # house_1 if house_n is robbed and vice versa. This puts us at two possible cases - one where
        # we rob house_1 but not house_n and vice versa. We just have to figure out the maximum of these two.
        return max(self.new_rob(nums[:-1]), self.new_rob(nums[1:]))
