object Solution {
    def isSymmetric(root: TreeNode): Boolean = {
        if (root == null) true else isMirror(root.left, root.right)
    }
    
    def isMirror(node1: TreeNode, node2: TreeNode): Boolean = {
        if (node1 == null && node2 == null) {
                true
            } else if ((node1 == null && node2 != null) || (node1 != null && node2 == null)) {
                false
            } else {
                node1.value == node2.value &&
                isMirror(node1.left, node2.right) &&
                isMirror(node1.right, node2.left)
            }
    }
}