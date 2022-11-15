class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 938.
# Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/
def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    self.res = 0

    def dfs(node):
        if not node:
            return 0
        if low <= node.val <= high:
            self.res += node.val

        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return self.res