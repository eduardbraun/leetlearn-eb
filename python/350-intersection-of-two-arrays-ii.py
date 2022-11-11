# 350.
# Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    nummap = {}
    res = []

    for num in nums1:
        nummap[num] = nummap.get(num, 0) + 1

    for num in nums2:
        if num in nummap and nummap[num] != 0:
            res.append(num)
            nummap[num] -= 1

    return res