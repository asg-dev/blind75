class Solution:
    # Time Complexity: O(m x n)
    # Space Complexity: O(m x n)
    # solution making use of a dp grid O(m x n)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        grid = [[0 for _ in range(n+1)] for __ in range(m+1)]

        for j in range(n-1, -1, -1):
            curr = [0 for _ in range(m+1)]
            for i in range(m-1, -1, -1):
                if text1[i] == text2[j]:
                    grid[i][j] = grid[i+1][j+1] + 1

                else:
                    grid[i][j] = max(grid[i+1][j], grid[i][j+1])

        return curr[0][0]

    # Time Complexity: O(m x n)
    # Space Complexity: O(n)
    # solution not making use of a dp grid - instead two arrays O(2n)
    def longestCommonSubsequence(self, text1: str, text2: str, without_grid: True) -> int:

        # specify m and n
        m = len(text1)
        n = len(text2)

        # set previous array as all 0s i.e. equivalent to the last row in the grid
        # notice the array size is the number of columns in the grid
        previous = [0 for _ in range(m+1)]

        # loop row times i.e. no of rows in the grid
        for j in range(n-1, -1, -1):

            # at each step, create a new array with 0s
            current = [0 for _ in range(m+1)]

            # for each character in both the strings
            for i in range(m-1, -1, -1):
                if text1[i] == text2[j]:
                    current[i] = previous[i+1] + 1
                else:
                    current[i] = max(current[i+1], previous[i])

            previous = current
        return previous[0]
