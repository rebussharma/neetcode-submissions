# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow, fast = head, head

        # while fast and fast.next: # fast.next can be null if no cycle but why check fast/
        #     slow = slow.next        # we check fast for null cuz in later step we update fast to fast.next.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         return True
        curr = head
        hs = set()
        while curr.next:
            if curr in hs:
                return True
            hs.add(curr)
            curr = curr.next
        return False
