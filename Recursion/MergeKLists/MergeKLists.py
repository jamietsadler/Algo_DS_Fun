from typing import ListNode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        return self.mergeListsRecursion(lists, 0, len(lists)-1)
    
    def mergeListsRecursion(self, lists, start, end):
        if start > end:
            return None
        if start == end:
            return lists[start]
        mid_idx = (start+end)//2
        leftList = self.mergeListsRecursion(lists, start, mid_idx)
        rightList = self.mergeListsRecursion(lists, mid_idx+1, end)
        return self.mergeLists(leftList, rightList)
        
        
    def mergeLists(self, l1, l2):
        dummy = curr = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if not l1:
            curr.next = l2
        else:
            curr.next= l1
        return dummy.next