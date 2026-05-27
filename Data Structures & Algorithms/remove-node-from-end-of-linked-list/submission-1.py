# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        l = dummy
        r = head

        while n > 0 and r:
            r = r.next
            n -= 1
        
        while r:
            l = l.next
            r = r.next

        l.next = l.next.next
        return dummy.next