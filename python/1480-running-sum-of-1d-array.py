# 1480.
# Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/
def runningSum(self, nums: List[int]) -> List[int]:
    sums = 0
    for i, n in enumerate(nums):
        sums += n
        nums[i] = sums

    return nums