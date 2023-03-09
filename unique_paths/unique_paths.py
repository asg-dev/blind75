class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1:
            return 1

        current_row = [1] * n

        # iterate m-1 times
        while m > 1:
            for i in range(n-2, -1, -1):
                # keep cumulative sum of array elements from reverse
                current_row[i] += current_row[i+1]
            m -= 1

        return current_row[0]
