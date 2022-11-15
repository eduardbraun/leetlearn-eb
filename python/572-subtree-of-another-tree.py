# 572.
# Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if subRoot is None:
        return True

    if root is None:
        return False

    def dfs(node, subNode) -> bool:
        if node is None and subNode is None:
            return True
        if node is None or subNode is None:
            return False

        if node.val != subNode.val:
            return False

        return dfs(node.left, subNode.left) and dfs(node.right, subNode.right)

    if root.val == subRoot.val and dfs(root, subRoot):
        return True

    return dfs(root.left, subRoot) or dfs(root.right, subRoot)
