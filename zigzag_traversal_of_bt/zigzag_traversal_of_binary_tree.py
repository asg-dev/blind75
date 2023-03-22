from collections import deque
from typing import List, Optional

from classdefs.tree_node import TreeNode


# Intuition: Perform level-order traversal but at each level reverse the level array based on a flag
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append(root)

        # traversing direction
        ltr = False

        zigzag_traversal = [[root.val]]

        while queue:
            size = len(queue)
            level = []

            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    level.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    level.append(node.right.val)

            if level:
                if ltr:
                    zigzag_traversal.append(level)
                else:
                    # reverse level if rtl
                    level.reverse()
                    zigzag_traversal.append(level)

            # flip direction
            ltr = not ltr

        return zigzag_traversal
