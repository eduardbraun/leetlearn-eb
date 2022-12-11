# 435.
# Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    # using sort it will first start with start value and if they overlap use the end value
    # we can also define which to sort using a lambda
    intervals.sort()
    res = 0

    prevEnd = intervals[0][1]
    # sind the numbers are [[1,2], [2,3]] we can use "start", "end"
    # intervals[1:] will start from index 1 sinde we already have index 0 at the beginning
    for start, end in intervals[1:]:
        if start >= prevEnd:
            prevEnd = end
        else:
            res += 1
            prevEnd = min(prevEnd, end)

    return res