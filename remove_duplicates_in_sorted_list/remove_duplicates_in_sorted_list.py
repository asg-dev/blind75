from typing import Optional

from classdefs.list_node import ListNode


# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # set a pointer to head
        ptr_1 = head

        # until we reach the end of the list
        while ptr_1:
            # set a pointer at the next step
            ptr_2 = ptr_1.next
            # since we have a sorted list, the duplicates always come beside the current element
            # keep pushing ptr_2 until we reach a non-duplicate
            while ptr_2 and ptr_1.val == ptr_2.val:
                ptr_2 = ptr_2.next
            # establish connection between current node and the current non-duplicate node
            ptr_1.next = ptr_2
            # move current node to current non-duplicate node to start doing the same thing again
            ptr_1 = ptr_2

        return head
