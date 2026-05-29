class TN:
    def __init__(self):
        self.child = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = TN()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.child:
                cur.child[c] = TN()
            cur = cur.child[c]

        cur.end = True

    def search(self, word: str) -> bool:

        def dfs(i, node):

            if i == len(word):
                return node.end

            c = word[i]

            if c == ".":
                for child in node.child.values():
                    if dfs(i + 1, child):
                        return True
                return False

            if c not in node.child:
                return False

            return dfs(i + 1, node.child[c])

        return dfs(0, self.root)