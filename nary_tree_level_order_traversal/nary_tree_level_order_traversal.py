from ast import List
from collections import deque

from classdefs.nary_node import Node


# Intuition: Same approach as in binary tree level order traversal, but instead of adding left
# and right, add all the children to the queue
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        level_order = [[root.val]]
        queue.append(root)

        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.popleft()
                # for all children in current node, process by adding into queue
                for child in node.children:
                    queue.append(child)
                    level.append(child.val)
            if level: level_order.append(level)

        return level_order
