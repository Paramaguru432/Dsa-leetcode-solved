# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while True:

            # Find the kth node
            kth = group_prev

            for i in range(k):

                kth = kth.next

                if kth is None:
                    return dummy.next

            group_next = kth.next

            # Reverse the group
            prev = group_next
            curr = group_prev.next

            while curr != group_next:

                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            # Move group_prev to the end of reversed group
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp

        