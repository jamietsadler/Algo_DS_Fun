from typing import TreeNode
from functools import cache

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        def helper(start, end):
            if start > end:
                return [None]
            if start == end:
                return [TreeNode(start)]
            ans = []
            for root in range(start, end+1):
                left_nodes = helper(start, root-1)
                right_nodes = helper(root+1, end)
                for leftNode in left_nodes:
                    for rightNode in right_nodes:
                        rootNode = TreeNode(root, leftNode, rightNode)
                        ans.append(rootNode)
            return ans
        
        return helper(1, n)

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        @cache
        def helper(start, end):
            if start > end:
                return [None]
            if start == end:
                return [TreeNode(start)]
            return [TreeNode(root, leftNode, rightNode) 
                        for root in range(start, end+1) 
                        for leftNode in helper(start, root-1) for rightNode in helper(root+1, end)]
        
        return helper(1, n)