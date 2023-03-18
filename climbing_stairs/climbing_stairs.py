# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        last = 1
        before_last = 1

        if n == 1:
            return 1

        # essentially a fibonacci series
        for i in range(2, n + 1):
            temp = last
            last = last + before_last
            before_last = temp

        return last
