# 150.
# Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
def evalRPN(self, tokens: List[str]) -> int:
    # create anew stack where we will store our results
    stack = []
    for c in tokens:
        if c == "+":
            # we pop twice get the values from the beginning of the stack and add them
            # then we append the result to the stack
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            # we pop twice get the values from the beginning of the stack and add them
            # then we append the result to the stack
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            # append the integer
            stack.append(int(c))
    # should be one value remaining in the stack which is the result
    return stack[0]
