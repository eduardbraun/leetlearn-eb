# 39.
# Combination Sum
# https://leetcode.com/problems/combination-sum/
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []

    # Backtracking
    def dfs(i, cur, total):
        # if we reached the target we append and return
        if total == target:
            res.append(cur.copy())
            return
        # if i is too large or bigger than target we return
        if i >= len(candidates) or total > target:
            return

        # append current set
        cur.append(candidates[i])

        # we don't increment i since we can use the same value multiple times
        dfs(i, cur, total + candidates[i])

        # pop and start from the next value
        cur.pop()
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res
