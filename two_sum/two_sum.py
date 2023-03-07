from typing import List


# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in index_map:
                return [index_map[complement], i]

            index_map[nums[i]] = i
