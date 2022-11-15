# 637.
# Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree/
def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    nodesQueue = deque([root])
    avgList = list()

    level_sum = 0

    # if root is null we return the empty list
    if root is None:
        return avgList

    # while nodes queue is not empty
    while nodesQueue:
        level_sum = 0
        # length of the queue
        size = len(nodesQueue)
        for i in range(size):

            # using normal queue is pop(0)
            node = nodesQueue.popleft()
            # sum up the value for that level
            level_sum += node.val
            # check if nodes have left or right then insert to queue for the next level
            # append will add to the right
            if node.left is not None:
                nodesQueue.append(node.left)
            if node.right is not None:
                nodesQueue.append(node.right)
        # calculate average and add to the list
        level_sum = float(level_sum) / size
        avgList.append(level_sum)
    return avgList