from typing import Optional, TreeNode

# Iterative
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        stack = [root, root]
        while stack:
            t1 = stack.pop(0)
            t2 = stack.pop(0)

            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            
            if t1.val != t2.val:
                return False

            stack.append(t1.left)
            stack.append(t2.right)
            stack.append(t1.right)
            stack.append(t2.left)

        return True


# Recursive
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root, root)
        
    def isMirror(self, root1, root2):
        if (root1 == None and root2 == None):
            return True
        if (root1 == None or root2 == None):
            return False
        return (root1.val == root2.val) and self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)
    
    