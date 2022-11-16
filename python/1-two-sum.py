# 1.
# Two Sum
# https://leetcode.com/problems/two-sum/
#
# Using a dictionary we can store a value does not yet exist with the index of the array,
# if the remaining is equals to one of the values in the dictionary we have ssolution
# since the solution is not sorted we can't use left, right pointer very efficiently
def twoSum(self, nums: List[int], target: int) -> List[int]:
    # dictionary
    rev_table = dict()
    for i in range(len(nums)):
        second_addend = target - nums[i]
        if second_addend in rev_table:
            return [rev_table[second_addend], i]
        else:
            rev_table[nums[i]] = i
