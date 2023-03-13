
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        stack = [(root, root.val)]

        while stack:
            root, total = stack.pop()
            if not root.right and not root.left:
                if total == targetSum:
                    return True
            if root.left:
                stack.append((root.left, total + root.left.val))
            if root.right:
                stack.append((root.right, total + root.right.val))   
        return False
            