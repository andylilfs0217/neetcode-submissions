# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 and list2 and list2.val > list1.val:
            list1, list2 = list2, list1

        ans = ListNode()
        ans_curr = ans
        curr1, curr2 = list1, list2

        while curr1 and curr2:
            if curr1.val < curr2.val:
                ans_curr.next = curr1
                curr1 = curr1.next
                ans_curr = ans_curr.next
            else:
                ans_curr.next = curr2
                curr2 = curr2.next
                ans_curr = ans_curr.next
        
        if curr1:
            ans_curr.next = curr1
        else:
            ans_curr.next = curr2

        ans = ans.next
        return ans