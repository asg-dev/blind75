from typing import List


# Time Complexity: O(n log n)
# Space Complexity: O(n)
class Solution:
    # binary search helper to find the immediately increasing element's index
    def binary_search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + (r - l) // 2)

            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return l

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # keep a dp array - which will contain the subsequence as we build it
        dp = [nums[0]]

        for i in range(1, n):
            if nums[i] > dp[-1]: # if current element is strictly increasing - append to dp list
                dp.append(nums[i])
            else:
                # replace the immediately largest element - since the dp array is guaranteed to be
                # sorted, we can run a binary search for the current element which will always return
                # the index of the immediate largest element (due to the nature of BS)
                replace_index = self.binary_search(dp, nums[i])
                dp[replace_index] = nums[i]

        # the current dp array is a valid LIS list if we want to see the contents
        print(dp)

        # just return the length - as per the question
        return len(dp)
