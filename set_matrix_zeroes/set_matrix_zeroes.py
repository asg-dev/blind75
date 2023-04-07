from typing import List

# Intuition: This is where we attempt to do the problem without extra space. We first mark all 0s to x
# then we iterate over the matrix and set the columns and rows to 0. Then, we change the matrix to reflect
# the first marked zeroes.

# Time Complexity: O(3 x m x n) => O(m x n)
# Space Complexity: O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        # mark existing zeroes in the array
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0: matrix[i][j] = 'x'

        for i in range(m):
            for j in range(n):
                # from starting point -> set all elements to the right to 0 if we encounter an x
                if matrix[i][j] == 'x':
                    r, c = i, j
                    while r < m:
                        if matrix[r][c] != 'x': matrix[r][c] = 0
                        r += 1
                    r, c = i, j
                    while r >= 0:
                        if matrix[r][c] != 'x': matrix[r][c] = 0
                        r -= 1
                    r, c = i, j
                    while c < n:
                        if matrix[r][c] != 'x': matrix[r][c] = 0
                        c += 1
                    r, c = i, j
                    while c >= 0:
                        if matrix[r][c] != 'x': matrix[r][c] = 0
                        c -= 1

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'x': matrix[i][j] = 0
