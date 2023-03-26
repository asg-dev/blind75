from typing import Optional
from classdefs.tree_node import TreeNode

# Intuition: This is similar to problem 'Same Tree' but with a small twist, we need to find where
# we should check for trees being same. This is done using a DFS approach - we perform DFS on the root
# to see where our subRoot starts from. Once we figure this out, we run same tree on that point.
# The one catch or gotcha here is that every time we set the Subtree (i.e.) find the subtree to be same
# we have to make sure that none of the other recursive paths we eventually go through can reset the subtree

# Time Complexity: O(n) where n is the no of nodes in root tree
# Space Complexity: O(h) where h is the height of the root tree
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.isSubtree = False
        self.dfs(root, subRoot)
        return self.isSubtree

    def dfs(self, root, subRoot):
        if not root:
            return

        self.dfs(root.left, subRoot)
        self.dfs(root.right, subRoot)

        # the not isSubtree condition makes sure that the flag is not reset (i.e.) we don't run isSameTree
        # again after we find a subtree (even if the root and subRoot values are same)
        if not self.isSubtree and root.val == subRoot.val:
            self.isSubtree = self.isSameTree(root, subRoot)
            return

    def isSameTree(self, p, q):
        if not p and not q: return True
        if not p and q or not q and p: return False
        if p.val != q.val: return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
