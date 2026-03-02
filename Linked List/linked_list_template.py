"""
=============================================================
LINKED LIST TEMPLATES
=============================================================
"""


# =============================================================
# BASIC NODE DEFINITION
# =============================================================
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# =============================================================
# 1. DUMMY HEAD (SIMPLIFY EDGE CASES)
# Use: when the head might change or be removed
# Examples: Remove Elements, Merge Lists, Insert Sorted
# =============================================================
def dummy_head_pattern(head):
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy

    while curr.next:
        if some_condition(curr.next):
            curr.next = curr.next.next  # skip/remove node
        else:
            curr = curr.next

    return dummy.next  # new head


# =============================================================
# 2. TWO POINTERS — FAST/SLOW (CYCLE DETECTION)
# Use: detect cycle, find cycle start, find middle
# Examples: Linked List Cycle, Linked List Cycle II
# =============================================================

# Detect cycle
def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Find cycle start
def find_cycle_start(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # move one pointer back to head
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow  # cycle start

    return None


# =============================================================
# 3. FIND MIDDLE NODE
# Use: split list in half, find middle element
# Examples: Middle of Linked List, Sort List, Palindrome List
# =============================================================

# Returns first middle (for even length: left middle)
def find_middle_left(head):
    slow = fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow  # left middle


# Returns second middle (for even length: right middle)
def find_middle_right(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow  # right middle


# =============================================================
# 4. REVERSE LINKED LIST
# Use: reverse entire list or portion of list
# Examples: Reverse Linked List, Reverse Linked List II,
#           Palindrome Linked List
# =============================================================

# Iterative
def reverse_list(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next   # save next
        curr.next = prev  # reverse pointer
        prev = curr       # move prev forward
        curr = nxt        # move curr forward

    return prev  # new head


# Recursive
def reverse_list_recursive(head):
    if not head or not head.next:
        return head

    new_head = reverse_list_recursive(head.next)
    head.next.next = head  # reverse the pointer
    head.next = None       # remove old pointer

    return new_head


# =============================================================
# 5. MERGE TWO SORTED LISTS
# Use: combine two sorted lists into one
# Examples: Merge Two Sorted Lists, Merge K Sorted Lists
# =============================================================
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 or l2  # attach remaining

    return dummy.next


# =============================================================
# 6. REMOVE NTH NODE FROM END
# Use: find/remove node at position from end
# Examples: Remove Nth Node From End, Kth From End
# =============================================================
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy

    # move fast n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next

    # move both until fast hits end
    while fast:
        slow = slow.next
        fast = fast.next

    # slow is now right before the target
    slow.next = slow.next.next

    return dummy.next


# =============================================================
# 7. INTERSECTION OF TWO LISTS
# Use: find where two lists meet
# Examples: Intersection of Two Linked Lists
# =============================================================
def get_intersection(headA, headB):
    a, b = headA, headB

    # when one reaches end, redirect to other list's head
    # they'll meet at intersection or both reach None
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA

    return a  # intersection node or None


# =============================================================
# 8. PALINDROME LINKED LIST
# Use: check if list reads same forwards and backwards
# Examples: Palindrome Linked List
# =============================================================
def is_palindrome(head):
    # step 1: find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # step 2: reverse second half
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    # step 3: compare both halves
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True


# =============================================================
# 9. SORT LIST (MERGE SORT)
# Use: sort a linked list in O(n log n)
# Examples: Sort List
# =============================================================
def sort_list(head):
    if not head or not head.next:
        return head

    # split in half
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None  # cut the list

    # sort each half
    left = sort_list(head)
    right = sort_list(mid)

    # merge
    return merge_two_lists(left, right)


# =============================================================
# 10. REORDER LIST
# Use: rearrange list alternating from both ends
# Examples: Reorder List (L0→Ln→L1→Ln-1→...)
# =============================================================
def reorder_list(head):
    if not head or not head.next:
        return

    # step 1: find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # step 2: reverse second half
    prev = None
    curr = slow.next
    slow.next = None  # cut
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # step 3: merge alternating
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2


# =============================================================
# CHEAT SHEET
# =============================================================
# Head might change/be removed     → 1. Dummy head
# Detect cycle / find cycle start  → 2. Fast-slow pointers
# Find middle of list              → 3. Fast-slow (half speed)
# Reverse a list                   → 4. Prev-curr-next pattern
# Combine two sorted lists         → 5. Merge with dummy head
# Find kth from end                → 6. Two pointers with gap
# Where two lists meet             → 7. Redirect at end
# Check palindrome                 → 8. Middle + reverse + compare
# Sort a linked list               → 9. Merge sort (split + merge)
# Rearrange from both ends         → 10. Middle + reverse + merge