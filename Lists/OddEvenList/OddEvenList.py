from typing import Optional, ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        curr = head
        even = head.next
        evenhead = even
        while even and even.next:
            curr.next = even.next
            curr = curr.next
            even.next = curr.next
            even = even.next
        curr.next = evenhead
        return head
            
            