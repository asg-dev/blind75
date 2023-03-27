from collections import deque
from typing import List

# Intuition: This is a BFS problem based on a 2D matrix. First, we iterate over the grid to see where
# the rotten oranges are, and push them to a queue. Then we process the queue - take each rotten orange,
# go level-order for each rotten orange, process their children (4 directional) i.e. rot them, and add
# to the queue. Repeat the process until queue is completely processed.

# Time Complexity: O(m x n)
# Space Complexity: O(m x n)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        fresh_count = 0
        time = -1
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: queue.append([i, j])
                elif grid[i][j] == 1: fresh_count += 1

        if fresh_count == 0: return 0

        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while queue:
            size = len(queue)
            time += 1
            for _ in range(size):
                i, j = queue.popleft()
                for ni, nj in dirs:
                    nr = i + ni
                    nc = j + nj
                    if 0 <= nr < m and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh_count -= 1
                            queue.append([nr, nc])

        return time if fresh_count == 0 else -1
