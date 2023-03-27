from typing import List

#Time Complexity: O(n)
#Space Complexity: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]

        for i in range(1, len(nums)):
            result.append(nums[i-1] * result[-1])

        suffix_prod = 1
        for i in range(len(result) - 2, -1, -1):
            result[i] *= nums[i + 1] * suffix_prod
            suffix_prod *= nums[i + 1]

        return result
