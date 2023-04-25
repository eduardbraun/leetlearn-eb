# 442.
# Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# O(m) time O(1) space complexety
def findDuplicates(self, nums: List[int]) -> List[int]:
    res = []

    for x in nums:
        if nums[abs(x) - 1] < 0:
            res.append(abs(x))
        # we negate all the values on x - 1 which we are guranteed to have a position in the array
        # if we visit that negated number again (x-1) we know for sure that x is a duplicate
        else:
            nums[abs(x) - 1] *= -1
    return res