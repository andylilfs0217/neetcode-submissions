# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode(next=head)

        r = start
        for _ in range(n):
            r = r.next
        l_prev, l, r = start, start.next, r.next

        while r:
            l_prev, l, r = l, l.next, r.next
        
        l_prev.next = l.next

        ans = start.next
        return ans