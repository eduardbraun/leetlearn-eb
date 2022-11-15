# 704.
# Binary Search
# https://leetcode.com/problems/binary-search/
def search(self, nums: List[int], target: int) -> int:
    start = 0
    end = len(nums)
    while start < end:
        mid = start + (end - start) // 2

        if (nums[mid] == target):
            return mid
        elif nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid
    return -1