# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        # SOL 1: 2 pass
        # if not head or not head.next:
        #     return None

        # dummy = ListNode()
        # dummy.next = head
        # size = 0
        # curr = head

        # while curr:
        #     curr = curr.next
        #     size += 1

        # curr = dummy

        # for i in range(size - n):
        #     curr = curr.next

        # # remove the next node
        # curr.next = curr.next.next

        # return dummy.next

        # SOL 2: 1 pass
        dummy = ListNode()
        dummy.next = head

        left = dummy
        right = dummy

        for i in range(n + 1):
            right = right.next

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next
