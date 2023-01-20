# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import TreeNode
class Solution:
    def __init__(self):
        self.ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurse(root):
            if not root:
                return False
            
            left = recurse(root.left)
            
            right = recurse(root.right)
            
            if p == root or q == root:
                mid = True
            else:
                mid = False
            
            if left + right + mid >= 2:
                self.ans = root
                
            return left or right or mid
        
        recurse(root)
        return self.ans


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        p_val = p.val
        q_val = q.val
        
        while root:
            if root.val > p_val and root.val > q_val:
                root = root.left
            elif root.val < p_val and root.val < q_val:
                root = root.right
            else:
                return root
            
        return None