from typing import List


# Time Complexity: O(n log n)
# Space Complexity: O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)

        # we sort the array initially - to allow us the ability to perform binary search later on
        nums.sort()

        result = []
        # essentially, this is a three pointer approach - we iterate through each element in nums,
        # fix one element and perform binary search (like) with two pointers for the rest of the elements
        for i in range(n-2):
            # handle duplicates here: skip to the last duplicate element
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # set start and end pointers for binary search
            j = i + 1
            k = n - 1
            # target is the complement of the current element we've fixed
            target = -1 * nums[i]

            while j < k:
                if (nums[j] + nums[k]) == target:
                    # we've reached a triplet
                    result.append([nums[i], nums[j], nums[k]])

                    # [IMP] handle duplicates: notice in the inner loop / two pointer part of the
                    # solution we handle duplicates then skip to the end.
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1

                    j += 1
                    k -= 1
                else:
                    if (nums[j] + nums[k]) > target:
                        k -= 1
                    else:
                        j += 1

        return result
