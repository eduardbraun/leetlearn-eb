# 169.
# Majority Element
# https://leetcode.com/problems/majority-element/
def majorityElement(self, nums: List[int]) -> int:
    num_dic = dict()

    for i in range(len(nums)):
        if nums[i] in num_dic:
            num_dic[nums[i]] = num_dic[nums[i]] + 1
        else:
            num_dic[nums[i]] = 1

        if num_dic[nums[i]] > len(nums) / 2:
            return nums[i]
    return nums[len(nums) - 1]