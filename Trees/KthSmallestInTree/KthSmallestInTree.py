from typing import Optional, TreeNode

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return None
        
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder_vals = []

        def inorder(node):
            if node.left:
                inorder(node.left)
            inorder_vals.append(node.val)
            if node.right:
                inorder(node.right)
            
        inorder(root)
        return inorder_vals[k-1]