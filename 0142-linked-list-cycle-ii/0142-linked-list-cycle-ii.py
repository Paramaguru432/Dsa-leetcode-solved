# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head

        # Step 1: Find whether a cycle exists
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        else:
            # No cycle
            return None

        # Step 2: Find the beginning of the cycle
        slow = head

        while slow != fast:

            slow = slow.next
            fast = fast.next

        return slow

        """
        :type head: ListNode
        :rtype: ListNode
        """
        