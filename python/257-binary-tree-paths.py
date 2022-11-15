class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 257.
# Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/
def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    if not root:
        return []
    # use collections dequeu instead of []
    res, queue = [], collections.deque([(root, "")])
    while queue:
        # dequeue will have both the node and the current str
        node, ls = queue.popleft()

        # we want to display to the furthest depth
        if not node.left and not node.right:
            res.append(ls + str(node.val))
        if node.left:
            queue.append((node.left, ls + str(node.val) + "->"))
        if node.right:
            queue.append((node.right, ls + str(node.val) + "->"))
    return res
