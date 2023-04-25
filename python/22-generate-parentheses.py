# 22.
# Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/
def generateParenthesis(self, n: int) -> List[str]:
    # only add open parenthesis if open < n
    # only add a closing parenthesis if closed < open
    # valid if open == closed == n
    stack = []
    res = []

    def backtrack(openN, closedN):
        # condition if open and close are == n
        if openN == n and closedN == n:
            res.append("".join(stack))
            return

        # if open is less then n we can add a parenthesis
        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()

        # if closedN is less than openN we can add a closed parenthesis
        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()

    backtrack(0, 0)
    return res