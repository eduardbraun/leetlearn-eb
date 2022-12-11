# 973.
# K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    minHeap = []

    for x, y in points:
        # we can use ** as the power of in python
        dist = (x ** 2) + (y ** 2)
        minHeap.append([dist, x, y])

    heapq.heapify(minHeap)

    res = []

    while k > 0:
        dist, x, y = heapq.heappop(minHeap)
        res.append([x, y])
        k -= 1
    return res