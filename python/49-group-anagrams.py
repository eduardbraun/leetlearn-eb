# 49.
# Group Anagrams
# https://leetcode.com/problems/group-anagrams/
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    curDict = dict()

    for i in range(len(strs)):
        strList = list(strs[i])
        strList.sort()

        strOrderd = ''.join(strList)

        if strOrderd in curDict:
            curDict[strOrderd].append(strs[i])
        else:
            curDict[strOrderd] = [strs[i]]

    return curDict.values()
