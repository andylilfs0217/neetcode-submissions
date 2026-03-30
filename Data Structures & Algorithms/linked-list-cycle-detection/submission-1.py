# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return False
        s, f = head.next, head.next.next
        while f:
            if s == f:
                return True
            else:
                s = s.next
                if f.next:
                    f = f.next.next
                else:
                    f = None
        return False