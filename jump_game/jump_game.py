# Intuition: We approach the problem from the last stair.

# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >=d:
                d = i

        return d == 0
