class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(l1, l2):
            # Dummy starter node
            dummy = ListNode(0)

            # Moving pointer
            tail = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next

                # Move tail forward
                tail = tail.next

            # One list may still have nodes left
            if l1:
                tail.next = l1

            if l2:
                tail.next = l2

            # Real merged list starts after dummy
            return dummy.next

        if not lists:
            return None

        res = lists[0]

        for i in range(1, len(lists)):
            res = merge(res, lists[i])

        return res