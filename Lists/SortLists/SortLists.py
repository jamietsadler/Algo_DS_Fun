from typing import Optional, ListNode
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(mid)

        return self.merge(l, r)

    def merge(self, left, right):
        if not left or not right:
            return left or right
        if left.val > right.val:
            right.next = self.merge(left, right.next)
            return right
        else:
            left.next = self.merge(left.next, right)
            return left