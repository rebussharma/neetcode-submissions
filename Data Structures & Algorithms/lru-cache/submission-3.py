class ListNode:
    """
    Doubly linked list node.

    Stores:
    - key   -> needed so we can remove from hashmap during eviction
    - val   -> actual cache value
    - prev  -> previous node in list
    - next  -> next node in list
    """

    def __init__(self, key: int, val: int):

        self.key = key
        self.val = val

        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):

        # maximum number of items allowed in cache
        self.cap = capacity

        # hashmap:
        # key -> linked list node
        #
        # allows O(1) lookup
        self.cache = {}

        # dummy head
        #
        # least recently used node
        # will always be right after head
        self.head = ListNode(-1, -1)

        # dummy tail
        #
        # most recently used node
        # will always be right before tail
        self.tail = ListNode(-1, -1)

        # connect dummy nodes
        self.head.next = self.tail
        self.tail.prev = self.head

    # ---------------------------------------------------------
    # PUBLIC METHODS
    # ---------------------------------------------------------

    def get(self, key: int) -> int:
        """
        Return value if key exists.
        Otherwise return -1.

        Accessing a key makes it recently used,
        so move node to MRU position.
        """

        # key not found
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # move node to MRU side
        self._remove(node)
        self._insert_mru(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        """
        Insert or update key/value pair.

        Newly inserted or updated node
        becomes most recently used.
        """

        # -------------------------------------------------
        # CASE 1:
        # key already exists
        #
        # remove old node first
        # -------------------------------------------------
        if key in self.cache:

            old_node = self.cache[key]

            self._remove(old_node)

            # remove old hashmap entry
            del self.cache[key]

        # -------------------------------------------------
        # create new node
        # -------------------------------------------------
        new_node = ListNode(key, value)

        # store in hashmap
        self.cache[key] = new_node

        # insert at MRU position
        self._insert_mru(new_node)

        # -------------------------------------------------
        # CASE 2:
        # capacity exceeded
        #
        # remove LRU node
        # -------------------------------------------------
        if len(self.cache) > self.cap:

            # first real node after dummy head
            # is always least recently used
            lru = self.head.next

            # remove from linked list
            self._remove(lru)

            # remove from hashmap
            del self.cache[lru.key]

    # ---------------------------------------------------------
    # PRIVATE HELPER METHODS
    # ---------------------------------------------------------

    def _insert_mru(self, node: ListNode) -> None:
        """
        Insert node right before dummy tail.

        Example:

        BEFORE:
        head <-> 1 <-> 2 <-> tail

        AFTER inserting 3:
        head <-> 1 <-> 2 <-> 3 <-> tail
        """

        # node currently before tail
        prev_node = self.tail.prev

        # connect prev_node -> node
        prev_node.next = node
        node.prev = prev_node

        # connect node -> tail
        node.next = self.tail
        self.tail.prev = node

    def _remove(self, node: ListNode) -> None:
        """
        Remove node from doubly linked list.

        Example:

        BEFORE:
        head <-> 1 <-> 2 <-> 3 <-> tail

        remove 2

        AFTER:
        head <-> 1 <-> 3 <-> tail
        """

        prev_node = node.prev
        next_node = node.next

        # bypass node
        prev_node.next = next_node
        next_node.prev = prev_node