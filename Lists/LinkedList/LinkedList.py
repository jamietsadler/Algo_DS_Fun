class ListNode(object):
    def __init__(self, val):
        self.next = None
        self.val = val    
    
class MyLinkedList(object):

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        # index steps needed 
        # to move from sentinel node to wanted index
        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return 
        if index < 0:
            index = 0
            
        prev = self.head
        for _ in range(index):
            prev = prev.next
            
        to_insert = ListNode(val)
        
        to_insert.next = prev.next
        prev.next = to_insert 
        self.size += 1        
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return 
        self.size -= 1
        prev = self.head
        
        for _ in range(index):
            prev = prev.next
        
        prev.next = prev.next.next
