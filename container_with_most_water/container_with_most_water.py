from typing import List


# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # define pointers for left and right
        l = 0
        r = len(height) - 1

        # keep track of maximum area encountered
        max_area = 0

        # notice the '<' sign - we don't have to process <= as we will need
        # at least one unit of breadth to attain area
        while l < r:
            # take the minimum height of each 'wall' and multiply with breadth to get area
            current_area = min(height[l], height[r]) * (r - l)
            max_area = max(current_area, max_area)

            # note: it doesn't matter if we move left or right if we encounter same height 'walls'
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
