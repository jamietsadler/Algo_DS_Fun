from typing import Optional, TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        curr_level = max_level = 1
        max_sum = float('-inf')
        queue = [root, ]
        
        while queue:
            # sum up all the nodes on the current level
            curr_sum = sum([x.val for x in queue])
            # update max_sum 
            if curr_sum > max_sum:
                max_sum, max_level = curr_sum, curr_level
            # build next level
            queue = [y for x in queue for y in [x.left, x.right] if y]
            curr_level += 1
            
        return max_level