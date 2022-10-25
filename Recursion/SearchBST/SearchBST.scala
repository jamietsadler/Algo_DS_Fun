/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
    def searchBST(root: TreeNode, `val`: Int): TreeNode = {
        if (root ==  null || root.value == `val`) return root
        
        if (root.value > `val`) return searchBST(root.left, `val`)
        else return searchBST(root.right, `val`)
    }
}


object Solution {
    def searchBST(root: TreeNode, `val`: Int): TreeNode = {
        if (root == null)
            null
        else
            root.value match {
                case `val` => root
                case x if x > `val` => searchBST(root.left, `val`)
                case x if x < `val` => searchBST(root.right, `val`)
            }
    }
}