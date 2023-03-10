from typing import List


# Time Complexity: O(m x n)
# Space Complexity: O(1)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        # specify m and n to start off the problem
        m = len(grid) # length of the grid is the number of rows
        n = len(grid[0]) # length of the nested arary is the number of columns

        # set the outer row
        for r in range(m-2, -1, -1):
            grid[r][n-1] += grid[r+1][n-1]

        # set the outer column
        for c in range(n-2, -1, -1):
            grid[m-1][c] += grid[m-1][c+1]

        # from the inner column, compute
        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                grid[r][c] += min(grid[r][c+1], grid[r+1][c])

        return grid[0][0]
