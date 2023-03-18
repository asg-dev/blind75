from typing import List


# Time Complexity: O(log n)
# Space Complexity: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        # essentially we do binary search here
        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] == target:
                return m

            # if: left sorted section
            if nums[l] <= nums[m]:
                # figure out if my target is in this range
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else: # right sorted section
                # figure out if my target is in this range
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1
