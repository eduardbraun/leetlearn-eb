# 128.
# Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

def longestConsecutive(self, nums: List[int]) -> int:
    # we have the set
    # now we just need to do a loop to check if it exists
    numSet = set(nums)
    longest = 0

    for i in range(len(nums)):
        # check if its the start of a sequence
        if (nums[i] - 1) not in numSet:
            length = 0
            while (nums[i] + length) in numSet:
                length += 1
            longest = max(length, longest)

    return longest