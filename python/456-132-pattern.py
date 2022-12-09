# 456.
# 132 Pattern
# https://leetcode.com/problems/132-pattern/
def find132pattern(self, nums: List[int]) -> bool:
    stack = []  # pair [num, minLeft], mono decreasing
    curMin = nums[0]

    # skip the first value since it cant be the k value
    for n in nums[1:]:
        while stack and n >= stack[-1][0]:
            stack.pop()
        if stack and n < stack[-1][0] and n > stack[-1][1]:
            return True

        stack.append([n, curMin])
        curMin = min(curMin, n)
    return False
