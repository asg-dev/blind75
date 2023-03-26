from classdefs.tree_node import TreeNode

# Intuition: Slightly trickier than the BST LCA, the BT LCA requires full search of the left and right
# subtrees. At each node, we see if we're the node we're looking for - if yes, we return that node.
# If I find my answer at both my left and right subtrees, then the current node is the answer. If I don't
# I just keep pushing my left of right up towards the root (it is guaranteed that I will find at least
# left or right)

# Time Complexity: O(n) where n is number of nodes
# Space Complexity: O(h) where h is height of the tree
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        # if I find the node I'm looking for (p or q), return this node
        # in turn, this node will be pushed up by the left and right ptrs
        if p.val == root.val or q.val == root.val:
            return root

        # search the left subtree for p or q
        left = self.lowestCommonAncestor(root.left, p, q)
        # search the right subtree for p or q
        right = self.lowestCommonAncestor(root.right, p, q)

        # if we found left AND right at THIS node, return THIS node => this is the answer
        # if we find left but not right and vice-versa, just keep pushing the found element (left or right) to the top.

        # one line but not very readable
        # return root if (left and right) else (left or right)

        if left and right: # final case: we have found the left and right at THIS node, so return THIS node as LCA
            return root

        if left or right: # intermediate case: we have found left but not right or vice-versa - just keep pushing that element up the recursive stack
            return left or right # similar to JS's left || right
