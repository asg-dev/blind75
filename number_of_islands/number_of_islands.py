from typing import List

# Intuition: This is a graph-based matrix problem. We perform DFS, going through each neigbor (4-directional)
# and keep filling water

# Time Complexity: O(m x n)
# Space Complexity: O(m x n)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.dirs = [[0,1],[1,0],[0,-1],[-1,0]]

        count=0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1

        return count

    def dfs(self,grid,i,j):
        if grid[i][j] == "0":
            return

        # fill the land with water
        grid[i][j] = "0"

        for ni,nj in self.dirs:
            nr = i+ni
            nc = j+nj
            if 0<=nr<self.m and 0<=nc<self.n:
                self.dfs(grid,nr,nc)
