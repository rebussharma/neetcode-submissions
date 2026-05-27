class ListNode():
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.res = [ListNode() for i in range(10**4) ]

    def put(self, key: int, value: int) -> None:
        index = key % len(self.res)
        cur = self.res[index]

        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        
        cur.next = ListNode(key, value)


    def get(self, key: int) -> int:
        index = key % len(self.res)
        cur = self.res[index].next

        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1   
            

    def remove(self, key: int) -> None:
        index = key % len(self.res)
        cur = self.res[index]

        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next