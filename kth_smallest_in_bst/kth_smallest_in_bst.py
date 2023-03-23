from typing import Optional

from classdefs.tree_node import TreeNode

# Intuition: Perform DFS / inorder traversal but decrement k at each step. This is based on the fact
# that performing inorder traversal on a binary search tree will always start from the smallest element.
# When k reaches 0, we'd have reached the kth smallest element.

# Time Complexity: O(n) if n is the number of nodes
# Space Complexity: O(h) if h is the height of the tree
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        self.smallest = root.val
        self.k = k
        self.dfs(root)
        return self.smallest

    def dfs(self, root):
        if root == None or self.k <= 0:
            return

        self.dfs(root.left)

        self.k -= 1
        if self.k == 0: self.smallest = root.val

        self.dfs(root.right)
