# 给定一份单词的清单，设计一个算法，创建由字母组成的面积最大的矩形，其中每一行组成一个单词(自左向右)，每一列也组成一个单词(自上而下)。不要求这些单词在清单里连续出现，但要求所有行等长，所有列等高。
#
# 如果有多个面积最大的矩形，输出任意一个均可。一个单词可以重复使用。
#
# 示例 1：
#
# 输入：["this", "real", "hard", "trh", "hea", "iar", "sld"]
# 输出：
# [
#    "this",
#    "real",
#    "hard"
# ]
# 示例 2：
#
# 输入：["aa"]
# 输出：["aa","aa"]
# 说明：
#
# words.length <= 1000
# words[i].length <= 100
# 数据保证单词足够随机


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





class Solution:
    def maxRectangle(self, words: List[str]) -> List[str]:
        mx = max(len(w) for w in words)
        tr = Trie()
        len_to_words = defaultdict(list)
        for w in words:
            tr.insert(w)
            len_to_words[len(w)].append(w)

        def search(node, ch: str):
            if ch in node:
                return node[ch]
            return None

        def calc(arr):
            # 计算由 arr 组成的最大矩阵，arr中的word都是相同长度
            m = len(arr[0])
            n = len(arr)
            res = 0
            matrix = []
            vis = []
            def dfs(pos):
                # mask 是选中arr的掩码，pos是列的trie中的节点列表
                nonlocal res, matrix
                n_vis = len(vis)
                for i in range(n):
                    pos1 = []
                    flg = True
                    end = True
                    for j in range(m):
                        v = search(pos[j], arr[i][j])
                        if v is None:
                            flg = False
                            break
                        if 'end' not in v:
                            end = False
                        pos1.append(v)
                    if flg:
                        vis.append(i)
                        if end:
                            if res < m * (n_vis + 1):
                                res = m * (n_vis + 1)
                                matrix = [arr[i] for i in vis]
                        dfs(pos1)
                        vis.pop()
            dfs([tr.root] * m)
            return res, matrix

        ans = 0
        mat = []
        for le in sorted(len_to_words.keys(), reverse=True):
            if le * mx <= ans: break  # 剪枝优化
            res, mt = calc(len_to_words[le])
            if res > ans:
                mat = mt
                ans = res
        return mat


so = Solution()
print(so.maxRectangle(["hv", "pi", "iu", "w", "yk", "lu", "dl", "e", "r", "pl"]))
print(so.maxRectangle(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(so.maxRectangle(["aa"]))
print(so.maxRectangle(["this", "real", "hard", "trh", "hea", "iar", "sld"]))


