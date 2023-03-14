from typing import Optional, TreeNode
from collections import deque

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.right = left
        root.left = right

        return root
    
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])

        while queue:
            curr = queue.popleft()
            curr.left, curr.right = curr.right, curr.left

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return root