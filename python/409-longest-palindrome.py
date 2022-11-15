# 409.
# Longest Palindrome
# https://leetcode.com/problems/longest-palindrome/
def longestPalindrome(self, s: str) -> int:
    hash = set()
    # we will use the hash set to fillter out the odd occurences
    # after that we can subtract the hashset which will have the odd once with the length of the str + 1 for one odd
    for c in s:
        if c not in hash:
            hash.add(c)
        else:
            hash.remove(c)
    # len(hash) is the number of the odd letters
    return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)
