# 136.
# Single Number
# https://leetcode.com/problems/single-number/
def singleNumber(self, nums: List[int]) -> int:
    # intuitive solution
    numset = set()
    for i in range(len(nums)):
        if nums[i] in numset:
            numset.remove(nums[i])
        else:
            numset.add(nums[i])

    if numset:
        return list(numset)[0]

    # other solution
    res = 0
    for num in nums:
        res ^= num
    return res