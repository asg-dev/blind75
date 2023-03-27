from collections import deque
from typing import List, Optional

from classdefs.tree_node import TreeNode

# Intuition: Using BFS, we go level after level and at each level, we append the last element
# to a resultant array.

# Time Complexity: O(n) where n is the number of nodes in the tree
# Space Complexity: O(h) where h is the height of the tree
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque()
        queue.append(root)
        right_view = []

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == size - 1 and node: right_view.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return right_view
