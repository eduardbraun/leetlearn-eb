class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 144.
# Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    res = []
    stack = [root]

    while stack:
        cur = stack.pop()
        res.append(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return res