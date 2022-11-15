# 141.
# Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/
def hasCycle(self, head):
    if head is None or head.next is None:
        return False

    slowPointer = head
    fastPointer = head.next

    while slowPointer.next is not None and fastPointer.next is not None and fastPointer.next.next is not None:
        if slowPointer == fastPointer:
            return True

        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
    return False