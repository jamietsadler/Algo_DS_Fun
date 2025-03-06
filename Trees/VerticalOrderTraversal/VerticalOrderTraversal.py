from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        hash_table = defaultdict(list)

        queue = [(root, 0)]
        col_1 = 0
        col_2 = 0

        while queue:
            node, column = queue.pop(0)
            if node:
                hash_table[column].append(node.val)
                col_1 = min(col_1, column)
                col_2 = max(col_2, column)
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        ans = [hash_table[x] for x in range(col_1, col_2+1)]
        return ans


