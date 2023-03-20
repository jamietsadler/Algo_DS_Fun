from typing import List, Optional, TreeNode

class Solution:
    def __init__(self):
        self.preorder_idx = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        

        def recurse(left, right):
            if left > right:
                return None
            val = preorder[self.preorder_idx]
            inorder_idx = inorder.index(val)

            root = TreeNode(val)
            self.preorder_idx += 1

            root.left = recurse(left, inorder_idx - 1)
            root.right = recurse(inorder_idx + 1, right)

            return root
            
    
        return recurse(0, len(preorder) - 1)