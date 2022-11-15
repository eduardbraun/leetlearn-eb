# 100.
# Same Tree
# https://leetcode.com/problems/same-tree/
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True

    if p is None and q is not None:
        return False

    if q is None and p is not None:
        return False

    if p.val != q.val:
        return False

    rightSame = self.isSameTree(p.left, q.left)
    leftSame = self.isSameTree(p.right, q.right)

    return rightSame and leftSame
