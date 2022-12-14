# 160.
# Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    if headA is None or headB is None:
        return None

    pa = headA  # 2 pointers
    pb = headB

    while pa is not pb:
        # if either pointer hits the end, switch head and continue the second traversal,
        # if not hit the end, just move on to next
        pa = headB if pa is None else pa.next
        pb = headA if pb is None else pb.next

    return pa  # only 2 ways to get out of the loop, they meet or the both hit the end=None