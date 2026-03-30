# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        digit = 0
        start = ListNode()
        curr = start
        while l1 and l2:
            total = l1.val + l2.val + carry
            carry = total//10
            digit = total%10
            node = ListNode(digit)
            curr.next = node
            curr = curr.next

            l1 = l1.next
            l2 = l2.next

        rl = l1 if l1 else l2
        while rl:
            total = rl.val + carry
            carry = total//10
            digit = total%10
            node = ListNode(digit)
            curr.next = node
            curr = curr.next

            rl = rl.next

        if carry > 0:
            node = ListNode(carry)
            curr.next = node
            curr = curr.next
        
        ans = start.next
        return ans

