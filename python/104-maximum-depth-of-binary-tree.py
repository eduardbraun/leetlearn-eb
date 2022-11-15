# 104.
# Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    def dfs(root, currentMax) -> int:
        if root is None:
            return currentMax

        currentMax += 1

        left_max = dfs(root.left, currentMax)
        right_max = dfs(root.right, currentMax)

        return max(left_max, right_max)

    max_left = dfs(root.left, 1)
    max_right = dfs(root.right, 1)
    return max(max_right, max_left)
