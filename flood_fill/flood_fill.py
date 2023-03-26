from typing import List

# Intuition: Very similar to 'Rotting Oranges' - we perform a dfs over the grid (neighbors) of the
# current index and convert the color - NOTE: we change it only if the neighbor is the same color of
# current index

# Time Complexity: O(m x n)
# Space Complexity: O(m x n)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.m = len(image)
        self.n = len(image[0])
        self.currentColor = image[sr][sc]
        self.image = image

        if color == self.currentColor:
            return image

        self.dfs(color, image[sr][sc], sr, sc)

        return image

    def dfs(self, color, currentColor, i, j):
        dirs = [[0, 1],[1, 0],[0, -1],[-1, 0]]

        self.image[i][j] = color
        for ni, nj in dirs:
            nr = i + ni
            nc = j + nj
            if 0 <= nr < self.m and 0 <= nc < self.n:
                if self.image[nr][nc] == currentColor:
                    self.dfs(color, self.image[nr][nc], nr, nc)
