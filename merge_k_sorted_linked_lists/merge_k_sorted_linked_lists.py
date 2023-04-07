from heapq import heappop, heappush

from classdefs.list_node import ListNode

# Intuition: This can be solved as an iterative 'merge two sorted lists' approach in O(nk) time, but
# we try to make it better by using a min-heap. The min-head simply tells us which element to add to our
# resultant list.

# Time Complexity: O(n log k)
# Space Complexity: O(k)
class Solution(object):
    def mergeKLists(self, lists):

        ListNode.__lt__ = lambda a,b : a.val < b.val

        result = ListNode(0)
        curr = result
        mheap = []

        for listhead in lists:
            if listhead:
                heappush(mheap,listhead)

        while mheap:
            element = heappop(mheap)

            if element.next:
                heappush(mheap, element.next)

            curr.next = element
            curr = curr.next

        return result.next
