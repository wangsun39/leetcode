# 请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。
#
# 实现词典类 WordDictionary ：
#
# WordDictionary() 初始化词典对象
# void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
# bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。
#
#
# 示例：
#
# 输入：
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# 输出：
# [null,null,null,null,false,true,true,true]
#
# 解释：
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // 返回 False
# wordDictionary.search("bad"); // 返回 True
# wordDictionary.search(".ad"); // 返回 True
# wordDictionary.search("b.."); // 返回 True
#
#
# 提示：
#
# 1 <= word.length <= 25
# addWord 中的 word 由小写英文字母组成
# search 中的 word 由 '.' 或小写英文字母组成
# 最多调用 104 次 addWord 和 search

from leetcode.allcode.competition.mypackage import *

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:  # O(log(len(word)))
        cur = self.root
        for e in word:
            if e not in cur:
                cur[e] = {}
            cur = cur[e]
        cur['end'] = True


    def search(self, word: str) -> bool:
        cur = self.root
        def dfs(nd, w):
            if w == '':
                return 'end' in nd
            for i, e in enumerate(w):
                if e == '.':
                    for x in nd.values():
                        if x == True: continue
                        if dfs(x, w[i + 1:]):
                            return True
                    return False
                else:
                    if e in nd:
                        nd = nd[e]
                    else:
                        return False
            return 'end' in nd
        return dfs(cur, word)

class WordDictionary:

    def __init__(self):
        self.tr = Trie()

    def addWord(self, word: str) -> None:
        self.tr.insert(word)

    def search(self, word: str) -> bool:
        return self.tr.search(word)

so = WordDictionary()
so.addWord('a')
so.addWord('a')
print(so.search('a.'))
print(so.search('.'))
print(so.search('aa'))
print(so.search('.a'))

so = WordDictionary()
so.addWord('bad')
so.addWord('dad')
so.addWord('mad')
print(so.search('pad'))
print(so.search('bad'))
print(so.search('.ad'))
print(so.search('d..'))

# Your Trie object will be instantiated and called as such:



