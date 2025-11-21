# 给定字典中的两个词，长度相等。写一个方法，把一个词转换成另一个词， 但是一次只能改变一个字符。每一步得到的新词都必须能在字典中找到。
#
# 编写一个程序，返回一个可能的转换序列。如有多个可能的转换序列，你可以返回任何一个。
#
# 示例 1：
#
# 输入：
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# 输出：
# ["hit","hot","dot","lot","log","cog"]
# 示例 2：
#
# 输入：
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# 输出：[]
#
# 解释：endWord "cog" 不在字典中，所以不存在符合要求的转换序列。


from leetcode.allcode.competition.mypackage import *

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        if endWord not in wordList: return []
        adj = defaultdict(set)
        for w in [beginWord] + wordList:
            for i in range(len(w)):
                adj[w[:i] + '*' + w[i + 1:]].add(w)
        pre = {}
        vis = {beginWord}
        dq = deque([beginWord])
        while dq:
            w = dq.popleft()
            for i in range(len(w)):
                w1 = w[:i] + '*' + w[i + 1:]
                for w2 in adj[w1]:
                    if w2 in vis: continue
                    dq.append(w2)
                    vis.add(w2)
                    pre[w2] = w
                    if w2 == endWord:
                        ans = [endWord]
                        while ans[-1] in pre:
                            ans.append(pre[ans[-1]])
                        return ans[::-1]
        return []


so = Solution()
print(so.findLadders(beginWord = "hit",endWord = "cog",wordList = ["hot","dot","dog","lot","log","cog"]))





