
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or k == 0 or not head.next:
            return head
        tmp = head
        n = 1
        while tmp.next:
            n += 1
            tmp = tmp.next
        
        k = k%n
        for _ in range(k):
            penultimate, last, = head, head.next
            while last.next is not None:
                penultimate = penultimate.next
                last = last.next

            last.next = head
            penultimate.next = None
            head = last

        return head