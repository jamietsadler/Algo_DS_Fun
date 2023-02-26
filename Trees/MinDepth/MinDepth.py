from typing import Optional, TreeNode
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(1, root)]
        min_depth = float("inf")

        while stack:
            depth, root = stack.pop()
            children = [root.left, root.right]
            if not any(children):
                min_depth = min(min_depth, depth)

            for c in children:
                if c:
                    stack.append((depth+1, c))

        return min_depth
    
# Recursion
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        children = [root.left, root.right]
        min_depth = float("inf")
        if not any(children):
            return 1

        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1

# BFS
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queue = deque([(1, root)])

        min_depth = float("inf")

        while queue:
            depth, root = queue.popleft()
            children = [root.left, root.right]
            if not any(children):
                return depth
            for c in children:
                if c:
                    queue.append((depth+1,c))