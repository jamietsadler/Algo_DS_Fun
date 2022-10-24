# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        firstNode = head
        secondNode = head.next
        
        firstNode.next = self.swapPairs(secondNode.next)
        secondNode.next = firstNode
        
        return secondNode