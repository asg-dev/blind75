
from typing import Optional

from classdefs.tree_node import TreeNode

# Intuition: Perform depth-first search and keep incrementing the depth at each node.
# Keep updating a global maximum and return the maximum at the end.

# Time Complexity: O(n) if n is the number of nodes in the tree
# Space Complexity: O(h) where h is height of the tree (call stack size)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        self.dfs(root, 1)
        return self.max_depth


    def dfs(self, root, depth):
        if not root:
            return

        self.max_depth = max(depth, self.max_depth)

        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)
