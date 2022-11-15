# 94.
# Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []

    def dfs(node):
        if node:
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

    dfs(root)
    return res
