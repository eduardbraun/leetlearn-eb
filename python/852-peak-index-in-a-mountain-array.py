# 852.
# Peak Index in a Mountain Array
# https://leetcode.com/problems/peak-index-in-a-mountain-array/
def peakIndexInMountainArray(self, arr: List[int]) -> int:
    low = 0
    high = len(arr)

    while low < high:
        # we use // to not get a floating pointer number but a full number
        mid = low + (high - low) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return low
