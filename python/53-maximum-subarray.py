# 53.
# Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxSub = nums[0]
    curSum = 0

    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSub = max(maxSub, curSum)

    return maxSub