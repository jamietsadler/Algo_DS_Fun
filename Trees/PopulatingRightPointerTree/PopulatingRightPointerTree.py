from typing import Optional
import collections

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root
        queue = collections.deque([root])
        while queue:           
            size = len(queue)
            for i in range(len(queue)):
                head = queue.popleft()
                if i < size - 1:
                    head.next = queue[0]
                if head.left:
                    queue.append(head.left)
                if head.right:
                    queue.append(head.right)
        return root