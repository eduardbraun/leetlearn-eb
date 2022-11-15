# 108.
# Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    if not nums:
        return None

    # first we need to find the root which should be mid of the array
    mid = len(nums) // 2
    root = TreeNode(nums[mid])

    # Get the left side which would be from start till mid of the array
    root.left = self.sortedArrayToBST(nums[:mid])
    # Get the right side which would be from the mid till the end of the array
    root.right = self.sortedArrayToBST(nums[mid + 1:])

    return root
