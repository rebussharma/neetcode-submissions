"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

    void add(key) Inserts the value key into the HashSet.
    bool contains(key) Returns whether the value key exists in the HashSet or not.
    void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

Example 1:

Input: ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]

Output: [null, null, null, true, false, null, true, null, false]

Explanation:
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1); // set = [1]
myHashSet.add(2); // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2); // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2); // set = [1]
myHashSet.contains(2); // return False, (already removed)

constrains:
size of set: could be any
number of keys: 0 <= key <= 1,000,000
total operations for add, remove, contains: 10,000
"""
class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

'''
    Solution:
    Need to implement hashset, cannot use pythons dictionary
    Closest DS we can use is array
    Array comes with 1 value and 1 index
        [5,4,3] has values 5,4,3 and index 0,1,2
    We also know that hasset also comes in KEY and Value format.
    For this question we have input paramater named 'key' in each method: add, contains, etc
    This  paramter can be named 'var' or 'num' or anything.
    Do not get confused with word 'key'

    we need to add this 'key' to out hashset. SInce hashset has key/value format:
    'key' param will be our value.
    What will be our ACTUAL KEY then?
        Simple, out ACTUAL KEY will be the remainder (modulo) of 'key' param and totoal number of items
        key % 10,000
        cuz modding 'key' by the size of key will always give us a number between 0 and 1,000,000
        1. key = 101    then actual key = 101 % 10000 = 1
        2. key = 1001   then actual key = 1001 % 10000 = 1
    Like above what happens if we get two params with % equal to 1?
    we will make 1 as out key and make both params 101 and 1001 linked listed values of 1

    SIZE here is 10,000 as question gives constrainst 10,000 as total operation, meaning if all operation is add we add 10,000 keys max.
    1000000 is NOT size its just a number


        
'''
class MyHashSet:
    def __init__(self):
        self.res = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        index = key % len(self.res)
        cur = self.res[index]

        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % len(self.res)
        cur = self.res[index]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        index = key % len(self.res)
        cur = self.res[index]

        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False