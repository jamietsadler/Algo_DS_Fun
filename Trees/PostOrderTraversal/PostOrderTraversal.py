from typing import Optional, TreeNode, List
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return None

        def helper(node, res):
            if node:
                helper(node.left, res)
                helper(node.right, res)
                res.append(node.val)
                
        helper(root, res)
        return res
    
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None
        stack = [(root, False)]
        output = []
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    output.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return output

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return None
        stack = [root]
        output = []

        while stack:
            node = stack.pop()
            if node:
                output.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return output[::-1]            
