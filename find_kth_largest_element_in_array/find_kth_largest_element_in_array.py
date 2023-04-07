from ast import List
from heapq import heappop, heappush

# Intuition: traditional heap problem. Create a min-heap that we will allow to rise until length k.
# ideally, we just keep track of k largest elements at any point.

# Time Complexity: O(n log k)
# Space Complexity: O(k)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []

        for num in nums:
            heappush(hp, num)
            if len(hp) > k:
                heappop(hp)

        return hp[0]
