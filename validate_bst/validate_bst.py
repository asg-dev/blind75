from typing import Optional

from classdefs.tree_node import TreeNode

# Intuition: Performing an inorder traversal on a valid binary search tree
# will return a sorted array

# Time Complexity: O(n), where n is the number of nodes in the tree
# Space Complexity: O(h), where h is the height of the tree
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = float("-inf")
        self.isValidBST = True

        self.inorder(root)

        return self.isValidBST

    # recursive function to perform inorder traversal
    def inorder(self, root):
        if not self.isValidBST or root == None:
            return False

        self.inorder(root.left)

        # processing: at each step, we check if the current node is greater than the previous node
        # if not, we set a global flag to be false
        if root.val <= self.prev:
            self.isValidBST = False
            return

        self.prev = root.val

        self.inorder(root.right)
