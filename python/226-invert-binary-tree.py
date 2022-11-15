# 226.
# Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    # BFS solution
    if root is None:
        return None

    queue = [root]

    while queue:
        node = queue.pop(0)
        left = node.left
        node.left = node.right
        node.right = left

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return root
