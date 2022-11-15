# 543.
# Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    self.ans = 0

    def height(p):
        # it's custom to define the height of an empty tree to be -1. This also fixes the off-by-one error I mentioned.
        if not p: return -1

        left, right = height(p.left), height(p.right)

        # the "2+" accounts for the edge on the left plus the edge on the right. This change is required to account for
        # the fact that we updated the height of an empty tree to be -1.
        self.ans = max(self.ans, 2 + left + right)

        return 1 + max(left, right)
    height(root)
    return self.ans
