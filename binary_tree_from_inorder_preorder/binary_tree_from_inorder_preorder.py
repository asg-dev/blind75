from typing import List, Optional

from classdefs.tree_node import TreeNode

# Intuition: We look at this problem as subproblems. We take each node and try to figure what the left
# and right subtrees of this node would be. Once we do that, we go inside each node and try to do the
# same.

# Time Complexity: O(n^2) [for each node, we do a linear search over inorder array to find pivot]
# TODO: Space Complexity:
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        pivot = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:pivot+1], inorder[:pivot])
        root.right = self.buildTree(preorder[pivot+1:], inorder[pivot+1:])
        return root
