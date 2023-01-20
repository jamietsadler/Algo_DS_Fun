from typing import TreeNode, Optional
import math

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, low = -math.inf, high = math.inf):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            
            return (helper(node.left, low, node.val) and helper(node.right, node.val, high))
        
        return helper(root)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = [(root, -math.inf, math.inf)]
        
        while stack:
            node, low, high = stack.pop()
            if not node:
                continue
            
            if node.val <= low or node.val >= high:
                return False
            stack.append((node.left, low, node.val))
            stack.append((node.right, node.val, high))
        
        return True
        