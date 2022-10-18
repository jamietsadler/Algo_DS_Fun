object Solution {
    def preorderTraversal(root: TreeNode): List[Int] = {
        if (root==null) List()
        else List(root.value) ++ preorderTraversal(root.left) ++ preorderTraversal(root.right)
    }
}