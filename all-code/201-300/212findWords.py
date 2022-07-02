from typing import List
class Node:
    def __init__(self, x):
        self.val = x
        self.next = {}
    def hasChildNode(self, v):
        return v in self.next.keys()

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

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def constructTree():
            obj = Trie()
            for w in words:
                obj.insert(w)
            return obj
        tree = constructTree()
        line, column = len(board), len(board[0])

        def tryOneNode(i, j, prefix, node):
            ret = node.hasChildNode(board[i][j])
            if not ret:
                return
            board[i][j], temp = '#', board[i][j]
            recurFind(i, j, prefix + temp, node.next[temp])
            if not node.next[temp].next:
                node.next.pop(temp)   # 前缀树剪枝
            board[i][j] = temp

        def recurFind(i, j, prefix, node):
            if node.hasChildNode(''):
                res.append(prefix)
                node.next.pop('')   # 前缀树剪枝
            if i > 0:
                tryOneNode(i - 1, j, prefix, node)
            if i < line - 1:
                tryOneNode(i + 1, j, prefix, node)
            if j > 0:
                tryOneNode(i, j - 1, prefix, node)
            if j < column - 1:
                tryOneNode(i, j + 1, prefix, node)
        res = []
        for i in range(line):
            for j in range(column):
                tryOneNode(i, j, '', tree.root)
        return res




so = Solution()

print(so.findWords([  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
], ["oath","pea","eat","rain"]))

