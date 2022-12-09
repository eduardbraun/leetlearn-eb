# 80.
# Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
def removeDuplicates(self, nums: List[int]) -> int:
    elmCount = {}
    count = 0
    i = 0

    while i < len(nums):
        elmCount[nums[i]] = 1 + elmCount.get(nums[i], 0)
        if elmCount[nums[i]] > 2:
            del nums[i]
            continue
        count += 1
        i += 1
    return count