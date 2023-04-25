# 238.
# Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
def productExceptSelf(self, nums: List[int]) -> List[int]:
    # [1, 2, 3, 4]
    res = [1] * len(nums)
    prefix = 1
    postfix = 1

    # we first calculate the prefix starting from one
    # [1, 1, 2, 6]
    for i in range(len(nums)):
        res[i] = prefix
        # multiply by the previous
        prefix *= nums[i]
    # we start from the end of the array (using range(length-1, -1, -1))
    # we multiply by the postfix starting from 1 and update the postfix
    # [ ,8 ,6]
    #           [1, 1, 2, 6]
    # postfix =  24, 12,4, 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res
