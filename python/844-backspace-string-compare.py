# 844.
# Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/
def backspaceCompare(self, s: str, t: str) -> bool:
    s_index = 0
    t_index = 0

    while s_index < len(s):
        if s[s_index] == '#' and s_index >= 1:
            s = s[:s_index - 1] + s[s_index + 1:]
            s_index -= 1
        elif s[s_index] == '#' and s_index == 0:
            s = s[:s_index] + s[s_index + 1:]
        else:
            s_index += 1

    while t_index < len(t):
        if t[t_index] == '#' and t_index >= 1:
            t = t[:t_index - 1] + t[t_index + 1:]
            t_index -= 1
        elif t[t_index] == '#' and t_index == 0:
            t = t[:t_index] + t[t_index + 1:]
        else:
            t_index += 1
    return s == t
