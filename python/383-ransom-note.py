# 383.
# Ransom Note
# https://leetcode.com/problems/ransom-note/
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    ranDict = dict()

    for c in ransomNote:
        ranDict[c] = ranDict.get(c, 0) + 1

    for c in magazine:
        if c in ranDict:
            if ranDict[c] == 1:
                del ranDict[c]
            else:
                ranDict[c] -= 1

    return len(ranDict) == 0