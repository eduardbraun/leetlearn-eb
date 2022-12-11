# 56.
# Merge Intervals
# https://leetcode.com/problems/merge-intervals/
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda i: i[0])
    # add first interval already to the result
    output = [intervals[0]]

    # we gona get the start and end values of the interval
    # we skip the first element that has already been added
    for start, end in intervals[1:]:
        # get the most recent interval
        lastEnd = output[-1][1]

        if start <= lastEnd:
            # if the overlap we increase the most recent interval end
            output[-1][1] = max(lastEnd, end)
        else:
            # if they do not overlap we add them to the output
            output.append([start, end])
    return output