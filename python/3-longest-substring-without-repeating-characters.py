# 3.
# Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
def lengthOfLongestSubstring(self, s: str) -> int:
    lettersUsed = set()
    maxCount = 0
    l = 0
    for i in range(len(s)):
        # letter is already in the set
        # l will always be at the start of the set and remove the first element until the duplicate is reached
        while s[i] in lettersUsed:
            lettersUsed.remove(s[l])
            l += 1

        # add letter to the set
        lettersUsed.add(s[i])

        # we check the max
        if len(lettersUsed) > maxCount:
            maxCount = len(lettersUsed)

    return maxCount