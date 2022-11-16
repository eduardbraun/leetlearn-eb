# 344.
# Reverse String
# https://leetcode.com/problems/reverse-string/
def reverseString(self, s: List[str]) -> None:
    left = 0
    right = len(s) - 1

    while left < right:
        curLeft = s[left]
        s[left] = s[right]
        s[right] = curLeft
        left += 1
        right -= 1