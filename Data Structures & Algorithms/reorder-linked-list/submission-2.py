# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head.next

        while f and f.next:
            s, f = s.next, f.next.next

        second = s.next # second half of the list
        s.next = None
        prev = None

        # reversing 2nd half of list
        while second:
            tmp = second.next
            second.next = prev

            prev = second
            second = tmp

        # merge two halves
        second = prev # head of second list
        # as prev will be set to last node and las node is the new head

        first = head

        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1

            first = t1
            second = t2

