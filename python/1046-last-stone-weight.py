# 1046.
# Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/
def lastStoneWeight(self, stones: List[int]) -> int:
    # turn min heap to max heap by multiplying by -1
    heap = [-1 * x for x in stones]
    heapq.heapify(heap)

    while len(heap) > 1:
        # remove two stones
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        if first != second:
            heapq.heappush(heap, first - second)

    if len(heap) == 0:
        return 0
    # get the value back by multiplying by -1
    return -1 * heap[0]