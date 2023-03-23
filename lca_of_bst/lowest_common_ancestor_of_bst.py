from classdefs.tree_node import TreeNode

# Intuition: This is an extremely intuitive problem. There is no coding gotchas here, however, the
# catch is in the way ancestors are present in a BST. Since we have a BST, we make two broad assumptions,
# if my p and q values are less than my current node, I move left. Else if my p and q values are greater
# than my current node, I move right. If one of the values is greater and the rest is smaller, I simply
# return that root because we shouldn't go beyond this depth.

# Time Complexity: O(log n) / O(h) where n is the number of nodes and h is the height of tree
# Space Complexity: O(1) [ as this is an iterative approach ]
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
