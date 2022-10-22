from typing import Optional, ListNode

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        
        value = 0 if val != 0 else 1
        psuedohead = ListNode(value)
        
        psuedohead.next = head
        
        prev, curr = psuedohead, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            
        return psuedohead.next