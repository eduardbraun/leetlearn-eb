# 557.
# Reverse Words in a String III
# https://leetcode.com/problems/reverse-words-in-a-string-iii/
def reverseWords(self, s: str) -> str:
    left = 0
    right = -1
    newS = list(s)

    for i in range(len(s)):
        if s[i] == " " or i == len(s) - 1:
            if (i == len(s) - 1):
                right += 1
            while left < right:
                curLeft = newS[left]
                newS[left] = newS[right]
                newS[right] = curLeft
                left += 1
                right -= 1
            left = i + 1
            right = i
        else:
            right += 1
    return ''.join(newS)
