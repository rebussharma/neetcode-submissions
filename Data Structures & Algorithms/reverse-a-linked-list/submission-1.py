# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
            head -> 0,1,2,3->null
        '''
        '''
                head->0->1->2->3->null
                null<-0<-1<-2<-3-<head
        '''
        prev = None
        cur = head
        
        while cur != None:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev
