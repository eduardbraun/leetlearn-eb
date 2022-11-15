# 26
# Remove duplicate
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
def removeDuplicates(self, nums: List[int]) -> int:
    index = 1
    while True:
        if index > len(nums) - 1:
            return len(nums)
        if nums[index - 1] == nums[index]:
            nums.pop(index)
        else:
            index += 1