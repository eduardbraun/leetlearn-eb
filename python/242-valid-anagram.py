# 242.
# Valid Anagram
# https://leetcode.com/problems/valid-anagram/
def isAnagram(self, s, t):
    stringDic = dict()

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        if s[i] in stringDic:
            stringDic[s[i]] += 1
        else:
            stringDic[s[i]] = 1

    for i in range(len(t)):
        if t[i] in stringDic:
            if stringDic[t[i]] == 0:
                return False
            else:
                stringDic[t[i]] -= 1
        else:
            return False
    return True