# Definition for singly-linked list.
from typing import Optional

from classdefs.list_node import ListNode


# Time Complexity: if m is number of nodes in list1 and n is list of nodes in list2, O(m) or O(n) whichever is greater
# Space Complexity: O(1)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node which will be the head of our new sorted list
        dummy = ListNode()
        # current node to iterate through the linked lists
        curr = dummy

        # until we reach the end of at least one node
        while list1 and list2:
            if list1.val < list2.val:
                # current's next will become the lesser value i.e. list1 in this case
                curr.next = list1
                # push current one level
                curr = list1
                # push list1 one level
                list1 = list1.next
            else:
                # current's next will become the greater value i.e. list2 in this case
                curr.next = list2
                # push current one level
                curr = list2
                # push list2 one level
                list2 = list2.next

        # if we reach the end, the rest of whichever list remains can just be appended to our new list
        if list1 or list2:
            curr.next = list1 if list1 else list2

        # notice here, we don't return dummy as the head node does not count - it simply contains 0
        return dummy.next
