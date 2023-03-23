from typing import Optional

from classdefs.list_node import ListNode

# Intuition: Keep two pointers (slow and fast) where the slow pointer moves one step at a time while

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        fast = head
        slow = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
