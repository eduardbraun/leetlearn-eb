# 876.
# Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slowPointer = head
    fastPointer = head

    while fastPointer.next is not None:
        if (fastPointer.next.next is None):
            return slowPointer.next
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
    return slowPointer
