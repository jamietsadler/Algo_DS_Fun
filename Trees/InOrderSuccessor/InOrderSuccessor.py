from typing import Optional, TreeNode

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        successor = None
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                successor = root
                root = root.left
            
        return successor

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None
        res = []
        def helper(node):
            if node:
                helper(node.left)
                res.append(node)
                helper(node.right)
        
        helper(root)
        
        for i in range(len(res)):
            if res[i].val == p.val:
                if i < len(res) - 1:
                    return res[i+1]
                else:
                    return None