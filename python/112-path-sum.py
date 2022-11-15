# 112.
# Path Sum
# https://leetcode.com/problems/path-sum/
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    if root is None:
        return False

    if root.left is None and root.right is None and targetSum - root.val == 0:
        return True

    return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
