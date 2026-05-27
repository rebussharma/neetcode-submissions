# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current: # prev<[0,1,2,3]
            # we need to remove the link from 0 and reverse that link
            # to remove the code is: current.next = prev. Now the link is reversed and pointing to previous.
            # BUT doing ONLY this will break the link from 0 to 1 and we will NOT be able to
            # traverse the rest of the liked list [1,2,3].
            #
            # So, we need to save the the link somehere. current.next is copied and saved to a varible before reversing.
            nxt = current.next # preserve link before breaking
            current.next = prev # reverse the link

            # Below statements are just to update variables
            # we need to update current to go to next and update previous to go to current
            prev = current
            current = nxt
        return prev
            