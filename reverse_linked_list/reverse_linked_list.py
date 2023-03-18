from typing import Optional

from classdefs.list_node import ListNode


# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        # until current reaches null
        while current != None:
            # set reference to the next
            temp = current.next

            current.next = previous
            # move previous one step
            previous = current
            # set new current
            current = temp

        return previous
