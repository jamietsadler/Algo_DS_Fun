# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return None
        
        firstHalfEnd = self.endOfFirstHalf(head)
        secondHalf = self.reverseList(firstHalfEnd.next)
        while secondHalf:
            if head.val != secondHalf.val:
                return False
            head = head.next
            secondHalf = secondHalf.next
        return True
        
        
        
    def endOfFirstHalf(self, head):
        slow = head
        fast = head
        
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next            
        return slow
            
    def reverseList(self, head):
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
            
