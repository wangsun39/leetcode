class Node:
    def __init__(self, x):
        self.val = x
        self.next = {}

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(None)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for letter in word:
            if letter not in cur.next:
                cur.next[letter] = Node(letter)
            cur = cur.next[letter]
        cur.next[''] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for letter in word:
            if letter not in cur.next:
                return False
            cur = cur.next[letter]
        if '' in cur.next:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for letter in prefix:
            if letter not in cur.next:
                return False
            cur = cur.next[letter]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("abc")
print(obj.search("abc"))
print(obj.startsWith("ab"))
print(obj.startsWith("abd"))


