# 231.
# Power of Two
# https://leetcode.com/problems/power-of-two/
def isPowerOfTwo(self, n: int) -> bool:
    return n and not (n & n - 1)