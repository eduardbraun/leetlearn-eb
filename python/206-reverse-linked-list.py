# 206.
# Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev

    return head