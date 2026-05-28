class TN:
    def __init__(self):
        self.child = {}
        self.endOfWord = False
class PrefixTree:

    def __init__(self):
        self.root = TN()
        
    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.child:
                cur.child[c] = TN()
            cur = cur.child[c] # moving the node
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.child:
                return False
            cur = cur.child[c]
        return cur.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.child:
                return False
            cur = cur.child[c]
        return True
        
        