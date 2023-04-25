# Combination Sum III
# https://leetcode.com/problems/combination-sum-iii/
def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    ret = []
    # create new list going from 1 - 9
    self.dfs(list(range(1, 10)), k, n, [], ret)
    return ret


def dfs(self, nums, k, n, path, ret):
    # if k or n are less then 0 we know the combination did not work and break the backtracking
    if k < 0 or n < 0:
        return
    # if n and k are 0 we know we have combination that worked
    if k == 0 and n == 0:
        ret.append(path)

    # go through nums
    for i in range(len(nums)):
        self.dfs(nums[i + 1:], k - 1, n - nums[i], path + [nums[i]], ret)