# 617.
# Merge Two Binary Trees
# https://leetcode.com/problems/merge-two-binary-trees/
def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if root1 is None and root2 is None:
        return root1

    if root1 and root2 is None:
        return root1

    if root2 and root1 is None:
        return root2

    root1.val += root2.val

    if root1.left or root2.left:
        root1.left = self.mergeTrees(root1.left, root2.left)
    if root1.right or root2.right:
        root1.right = self.mergeTrees(root1.right, root2.right)
    return root1
