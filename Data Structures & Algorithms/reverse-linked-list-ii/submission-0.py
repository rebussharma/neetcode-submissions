# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # dummy.next = head

        leftPrev, cur = dummy, head
        '''
            0->1->2->3->4->5 left = 1, right = 4

            lets set our leftPrev to(0) one item before 1
        '''
        for i in range(left-1): # executes once, leftPrev gets set to 0, cur to 1
            leftPrev, cur = cur, cur.next

        # lets reverse the list
        prev = None
        for i in range( right - left + 1): # +1 as we have to go past right

            # from loop above cur is at 1
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp # move cur along

        '''
         tillNow we have
            leftPrev at 0, so leftPrev.next is pointing at 1
            cur at 1 item past right: 5
            prev = 4
        
        original:       0->1->2->3->4->5
        what we want:   0->4->3->2->1->5

        what we have 0 4->3->2->1
        
        we need to point 0 to 4 leftPrev to prev
        we need to point 1 to 5
        1 is leftPrev.next, so we need 1.next to poin to 5
        leftPrev.next.next = cur
        '''

        leftPrev.next.next = cur # 1 points to 5
        # also need leftPrev (0) to point to 4
        leftPrev.next = prev

        return dummy.next