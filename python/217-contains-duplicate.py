# 217.
# Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    hashSet = set()

    for i in range(len(nums)):
        if (nums[i] in hashSet):
            return True
        hashSet.add(nums[i])
    return False