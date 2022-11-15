# 111.
# Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/
def minDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    depth = 1
    queue = [root]
    # Go through the queue till empty
    while queue:
        # size of the queue
        size = len(queue)
        for i in range(size):
            # we always want to pop from the left so we need to do pop(0)
            # if we leave pop() it will pop from the right
            node = queue.pop(0)

            # if both left and right is empty we reached the min depth
            if node.left is None and node.right is None:
                return depth
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        # increase the depth
        depth += 1
    # should never reach that if the nodes always have a depth
    return depth
