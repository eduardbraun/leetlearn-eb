# 977.
# Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/
def sortedSquares(self, nums: List[int]) -> List[int]:
    start = 0
    end = len(nums) - 1
    result = [None for y in range(len(nums))]
    # we start from the end
    # if start is bigger then end start will be at the end
    # we +1 start -1 end when a number is added
    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[start]) > abs(nums[end]):
            result[i] = nums[start] * nums[start]
            start += 1
        else:
            result[i] = nums[end] * nums[end]
            end -= 1
    return result
