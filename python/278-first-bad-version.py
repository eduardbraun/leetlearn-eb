# 278.
# First Bad Version
# https://leetcode.com/problems/first-bad-version/
def firstBadVersion(self, n: int) -> int:
    start = 1
    end = n

    if n == 1 and isBadVersion(n):
        return n

    while start < end:
        mid = start + (end - start) // 2

        if (isBadVersion(mid)):
            end = mid
        else:
            start = mid + 1
    return start
