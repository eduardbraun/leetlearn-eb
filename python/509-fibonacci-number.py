# 509.
# Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/
def fib(self, n: int) -> int:
    memo = {}

    def calcFib(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        #   if N-1 not in memo: memo[N-1] = fib(N-1)
        # 	if N-2 not in memo: memo[N-2] = fib(N-2)
        if n - 1 not in memo:
            memo[n - 1] = calcFib(n - 1)
        if n - 2 not in memo:
            memo[n - 2] = calcFib(n - 2)

        return memo[n - 1] + memo[n - 2]

    return calcFib(n)
