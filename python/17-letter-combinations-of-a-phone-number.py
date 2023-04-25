# 17.
# Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
def letterCombinations(self, digits: str) -> List[str]:
    digitToChar = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "qprs",
        "8": "tuv",
        "9": "wxyz",
    }

    res = []

    def backtrack(i, curStr):
        # if we reached the result length
        if len(curStr) == len(digits):
            res.append(curStr)
            return

        # n = "23"
        # 2 = "abc"
        # 3 = "def"
        for c in digitToChar[digits[i]]:
            # ad, ae, af, bd, be,bf, cd,ce,cf
            backtrack(i + 1, curStr + c)

    if digits:
        backtrack(0, "")
    return res