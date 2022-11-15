# 101.
# Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return False

    def dfs(leftNode, rightNode):

        if rightNode is None or leftNode is None:
            return rightNode == leftNode

        if leftNode.val != rightNode.val:
            return False

        return dfs(leftNode.left, rightNode.right) and dfs(leftNode.right, rightNode.left)

    return dfs(root.left, root.right)
