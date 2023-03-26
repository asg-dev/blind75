from typing import Optional
from classdefs.tree_node import TreeNode

# Intuition: We recursively go through the tree and check at each step if both trees are same.
# The special case is when one hits null and the other does not - this is when we return False
# Due to the and operator on the return statement, a false statement bubbling up would make sure
# we return false.

# Time Complexity: O(n) where n is the number of nodes in the tree
# Space Complexity: O(h) where h is the height of the tree
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p and q or not q and p:
            return False

        if p.val != q.val: return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
