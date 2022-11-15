# 1929.
# Concatenation of Array
# https://leetcode.com/problems/concatenation-of-array/
def getConcatenation(self, nums: List[int]) -> List[int]:
    ans = [None for y in range((len(nums) * 2))]
    index = 0

    for i in range(len(ans)):
        if (i >= len(nums)):
            ans[i] = nums[index]
            index += 1
        else:
            ans[i] = nums[i]

    return ans