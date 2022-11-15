# 14.
# Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
def longestCommonPrefix(self, strs: List[str]) -> str:
    curSubString = ""
    count = 0
    while True:
        if count >= len(strs[0]):
            return curSubString
        cur = strs[0][count]
        for i in range(len(strs)):
            if count >= len(strs[i]) or strs[i][count] != cur:
                return curSubString
        curSubString += cur
        count += 1