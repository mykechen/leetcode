# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        # step 1: find middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # step 2: reverse second half
        prev, cur = None, slow.next
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        slow.next = None

        # step 3: merge lists
        head1, head2 = head, prev
        while head1 and head2:
            next1 = head1.next
            next2 = head2.next

            head1.next = head2
            head1 = next1

            head2.next = head1
            head2 = next2

        