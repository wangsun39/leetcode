# 给你一个包含 n 个 互不相同 字符串的数组 words，这些字符串仅由从 'a' 到 'j' 的小写英文字母组成。另给你一个整数数组 target，其中每个从 0 到 n - 1 的下标都恰好出现一次。
#
# 利用 words 构建一棵 前缀树 ：
#
# 根节点表示空字符串 ""。
# 每个其他节点表示单词中一个不同的非空前缀。一个节点的父节点是通过移除其最后一个字符后得到的前缀。
# 表示完整单词 words[i] 的节点被标记为下标 i。被标记的节点也可以拥有子节点。
# 你可以 独立地 选择 每个节点 内子节点的访问顺序。但不能改变哪个节点是子节点的父节点。
#
# 从根节点开始遍历前缀树。在访问一个节点时，若该节点被标记，则先记录它的下标。然后按照选定的顺序访问它的子节点，在移动到下一个子节点之前，先完成对当前子节点树的遍历。这是一种 先序遍历 。
#
# 记录标记的下标构成一个长度为 n 的数组 traversal。设 pos[i] 为下标 i 在 target 中的位置。
#
# 一个 逆序对 是一对位置 (a, b)，满足 0 <= a < b < n 且 pos[traversal[a]] > pos[traversal[b]]。
#
# 返回在所有子节点顺序的选择下，可能达到的最小逆序对数量。
#
# 字符串的 前缀 是指通过从该字符串的末尾移除零个或多个字符而获得的字符串。
#
#
#
# 示例 1：
#
#
#
# 输入： words = ["bad","bag","fig","fed"], target = [3,1,0,2]
#
# 输出： 2
#
# 解释：
#
# 先访问根节点的 "f" 子节点，然后再访问 "b" 子节点。在 "f" 分支内部，先访问 "fed" 再访问 "fig"。在 "b" 分支内部，先访问 "bag" 再访问 "bad"。
#
# 这将产生 traversal = [3,2,1,0]：
#
# 遍历位置	单词下标	单词	在 target 中的位置
# 0	3	"fed"	0
# 1	2	"fig"	3
# 2	1	"bag"	1
# 3	0	"bad"	2
# 在 target 中的位置分别为 [0,3,1,2]。逆序对是 遍历位置 的对 (1,2) 和 (1,3)，因为 3 > 1 且 3 > 2。
#
# 没有任何子节点排序可以产生少于 2 个的逆序对。
#
# 示例 2：
#
# 输入： words = ["ab","ac","ba","bc"], target = [0,3,1,2]
#
# 输出： 1
#
# 解释：
#
# 先访问根节点的 "a" 子节点，然后再访问 "b" 子节点。在这些分支内部，先访问 "ab" 再访问 "ac"，以及先访问 "bc" 再访问 "ba"。
#
# 这将产生 traversal = [0,1,3,2]：
#
# 遍历位置	单词下标	单词	在 target 中的位置
# 0	0	"ab"	0
# 1	1	"ac"	2
# 2	3	"bc"	1
# 3	2	"ba"	3
# 在 target 中的位置分别为 [0,2,1,3]。唯一的逆序对是 遍历位置 的对 (1,2)，因为 2 > 1。
#
# 没有任何子节点排序可以产生 0 个逆序对。
#
#
#
# 提示：
#
# 1 <= n == words.length <= 104
# 1 <= words[i].length <= 20
# words[i] 仅包含从 'a' 到 'j' 的小写英文字母
# 所有 words[i] 都是 唯一 的
# 0 <= target[i] <= n - 1
# target 是 0 到 n - 1 整数的一个排列

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a

class Trie:

    def __init__(self):
        self.root = {}
        # self.pos = -1  # 在 target 中的地址
        self.ans = 0

    def insert(self, word: str, pi) -> None:  # O(log(len(word)))
        cur = self.root
        for e in word:
            if e not in cur:
                cur[e] = {}
            cur = cur[e]
        # cur['end'] = True
        cur['pos'] = pi  # word 在 target 中的下标

    def solve(self):  # DFS 处理 Trie 树上的各个节点
        def inv_pairs(a1, a2):
            # 计算两个排序数组，先a1后a2  可能产生的逆序对数量
            # a1 在 a2 之前
            p1 = r = 0
            for p2 in range(len(a2)):
                while p1 < len(a1) and a2[p2] > a1[p1]:
                    p1 += 1
                if p1 == len(a1):
                    break
                r += len(a1) - p1
            return r


        def dfs(nd1):
            # 返回当前节点下有哪些word，返回一个有序的 word 对应的 pos 数组
            arr = []  # 所有子节点 dfs 的返回值数组
            res = []
            for key, nd2 in nd1.items():
                if key not in {'pos'}:
                    arr2 = dfs(nd2)
                    arr.append(arr2)
                    res += arr2

            na = len(arr)
            inv = [[0] * na for _ in range(na)]
            for i in range(na):
                for j in range(i + 1, na):
                    inv[i][j] = inv_pairs(arr[i], arr[j])
                    inv[j][i] = len(arr[i]) * len(arr[j]) - inv[i][j]
            dp = [inf] * (1 << na)  # 状压DP
            dp[0] = 0
            for i in range(1, 1 << na):  # 计算一组子树的最小逆序对，掩码是 i
                ids = [ii for ii in range(na) if i & (1 << ii)]   # 先取出所有可能下标，没有这步通过不了
                for j in ids:  # 枚举子树j， 将子树j 放在这组子树的最后一个
                    cnt = dp[i ^ (1 << j)]
                    for k in ids:
                        if k != j:
                            cnt += inv[k][j]
                    dp[i] = MIN(dp[i], cnt)

            # ---- 下面注释内的是另一种优化，理论上更好，预计算 add[j][mask] ----
            # add = [[0] * (1 << na) for _ in range(na)]
            # for j in range(na):
            #     addj = add[j]
            #     for mask in range(1, 1 << na):
            #         low = mask & -mask
            #         k = low.bit_length() - 1
            #         addj[mask] = addj[mask ^ low] + (inv[k][j] if k != j else 0)
            #
            # # 状压DP，转移 O(1)
            # dp = [inf] * (1 << na)
            # dp[0] = 0
            # for mask in range(1, 1 << na):
            #     best = inf
            #     m = mask
            #     while m:
            #         low = m & -m
            #         j = low.bit_length() - 1
            #         prev = mask ^ low
            #         v = dp[prev] + add[j][prev]
            #         if v < best:
            #             best = v
            #         m ^= low
            #     dp[mask] = best
            # ---- 改到这里结束 ----


            self.ans += dp[-1]
            res.sort()
            if 'pos' in nd1:
                # 计算根节点与子树产生的所有逆序对数量
                ps = nd1['pos']
                p = bisect_left(res, ps)
                self.ans += p
                res = res[:p] + [ps] + res[p:]
            return res

        dfs(self.root)

class Solution:
    def minInversions(self, words: list[str], target: list[int]) -> int:
        n = len(words)
        pos = [0] * n
        for i, x in enumerate(target):
            pos[x] = i

        tr = Trie()
        for i, w in enumerate(words):
            tr.insert(w, pos[i])

        tr.solve()
        return tr.ans



so = Solution()
print(so.minInversions(words = ["ab","ac","ba","bc"], target = [0,3,1,2]))  # 1
print(so.minInversions(words = ["fiddiaehahbbhfddddd","gdfehhadebce","f","jahhaijcddidhe"], target = [2,3,0,1]))  # 1
print(so.minInversions(words = ["bad","bag","fig","fed"], target = [3,1,0,2]))  # 2



