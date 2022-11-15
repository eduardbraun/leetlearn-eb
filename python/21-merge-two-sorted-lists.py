# 21.
# Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy_node = ListNode(val=0)
    tail = dummy_node

    while list1 is not None and list2 is not None:
        if list1.val >= list2.val:
            tail.next = list2
            list2 = list2.next
        else:
            tail.next = list1
            list1 = list1.next

        tail = tail.next

    # check if list1 has a remaining
    if list1 is not None:
        tail.next = list1
    # check if list2 has a remaining
    elif list2 is not None:
        tail.next = list2

    return dummy_node.next
