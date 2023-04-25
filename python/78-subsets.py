#  78.
#  Subsets
# https://leetcode.com/problems/subsets/
def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []

    subset = []

    def dfs(i):
        if i >= len(nums):
            # if i reaches the end or is bigger we will insert the full subset
            res.append(subset.copy())
            return

        # decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)

        # decision not to include nums[i]
        # pop deletes from the right
        subset.pop()
        dfs(i + 1)

    dfs(0)

    return res