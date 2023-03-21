from collections import deque
from typing import List, Optional

from classdefs.tree_node import TreeNode

# Intuition: To perform a level-order traversal, we create a queue where we store each root
# and process their children.

# Time Complexity: O(n) if n is the number of nodes
# Space Complexity: O(2^h - 1) - the size the queue grows to
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque()
        queue.append(root)

        level_order = [[root.val]]
        while queue:
            level = []
            # IMPORTANT: this loop is important because we have to process each level
            # if we had to process each subtree instead, we wouldn't need this loop.
            # Until we process all elements for that level, we store the left and right
            # children values in a temporary array which we append to our original result
            for i in range(len(queue)):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                    level.append(current.left.val)
                if current.right:
                    queue.append(current.right)
                    level.append(current.right.val)

            if level: level_order.append(level)

        return level_order
