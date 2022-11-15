# 235.
# Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # if root.val > p.val and root.val > q.val:
    #     return self.lowestCommonAncestor(root.left, p, q)
    # elif root.val < p.val and root.val < q.val:
    #     return self.lowestCommonAncestor(root.right, p, q)
    # else:
    #     return root

    cur = root
    while cur:
        if p.val > cur.val and q.val > cur.val:
            cur = cur.right
        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left
        else:
            return cur