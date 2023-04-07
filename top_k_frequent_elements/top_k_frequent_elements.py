# Intuition: another min-heap approach with frequency map + bucket sort.

# Time Complexity: O(n log k)
# Space Complexity: O(n)
class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        n = len(nums)
        for num in nums:
          freq[num] = 1 if num not in freq else freq[num] + 1

        bucket = [[]] * (n+1)

        for key, v in freq.items():
            if not bucket[v]:
                bucket[v] = [key]
            else:
                bucket[v].append(key)

        result = []
        for i in range(len(bucket)-1, 0, -1):
            if bucket[i]:
                result += bucket[i]
                k -= len(bucket[i])

            if k==0:
                break

        return result
