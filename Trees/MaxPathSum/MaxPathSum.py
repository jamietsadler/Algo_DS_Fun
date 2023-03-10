class Solution(object):
    def __init__(self):
        self.max_sum = float("-inf")

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum(root)
        return self.max_sum


    def maxSum(self, root):
        if not root:
            return 0

        max_right_sum = max(self.maxSum(root.left), 0)
        max_left_sum = max(self.maxSum(root.right), 0)

        self.max_sum = max(self.max_sum, max_right_sum + max_left_sum + root.val)

        return max(max_right_sum + root.val, max_left_sum + root.val)