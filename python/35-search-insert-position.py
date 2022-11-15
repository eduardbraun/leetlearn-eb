# 35.
# Search Insert Position
# https://leetcode.com/problems/search-insert-position/
def searchInsert(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid - 1] < target < nums[mid]:
            return mid
        if target > nums[mid]:
            left = mid + 1
        if target < nums[mid]:
            right = mid
    return left
