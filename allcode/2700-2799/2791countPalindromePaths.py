# 给你一棵 树（即，一个连通、无向且无环的图），根 节点为 0 ，由编号从 0 到 n - 1 的 n 个节点组成。这棵树用一个长度为 n 、下标从 0 开始的数组 parent 表示，其中 parent[i] 为节点 i 的父节点，由于节点 0 为根节点，所以 parent[0] == -1 。
#
# 另给你一个长度为 n 的字符串 s ，其中 s[i] 是分配给 i 和 parent[i] 之间的边的字符。s[0] 可以忽略。
#
# 找出满足 u < v ，且从 u 到 v 的路径上分配的字符可以 重新排列 形成 回文 的所有节点对 (u, v) ，并返回节点对的数目。
#
# 如果一个字符串正着读和反着读都相同，那么这个字符串就是一个 回文 。
#
#
#
# 示例 1：
#
#
#
# 输入：parent = [-1,0,0,1,1,2], s = "acaabc"
# 输出：8
# 解释：符合题目要求的节点对分别是：
# - (0,1)、(0,2)、(1,3)、(1,4) 和 (2,5) ，路径上只有一个字符，满足回文定义。
# - (2,3)，路径上字符形成的字符串是 "aca" ，满足回文定义。
# - (1,5)，路径上字符形成的字符串是 "cac" ，满足回文定义。
# - (3,5)，路径上字符形成的字符串是 "acac" ，可以重排形成回文 "acca" 。
# 示例 2：
#
# 输入：parent = [-1,0,0,0,0], s = "aaaaa"
# 输出：10
# 解释：任何满足 u < v 的节点对 (u,v) 都符合题目要求。
#
#
# 提示：
#
# n == parent.length == s.length
# 1 <= n <= 105
# 对于所有 i >= 1 ，0 <= parent[i] <= n - 1 均成立
# parent[0] == -1
# parent 表示一棵有效的树
# s 仅由小写英文字母组成

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        s = [c2i[x] for x in s]  # 转换为数字
        g = defaultdict(list)
        n = len(parent)
        for i in range(n):
            g[parent[i]].append([i, s[i]])
        ans = 0
        values = [0] * n

        def dfs(x, acc):
            # 计算从0到x的路径上所有字母奇偶计数值，acc是之前的累计值
            for y, sxy in g[x]:
                values[y] = acc ^ (1 << sxy)
                dfs(y, values[y])
            return

        dfs(0, 0)
        counter = Counter()
        for i, x in enumerate(values):
            # 枚举每个点，哈希查找与其他点异或值相同或仅差异一个bit的数量
            ans += counter[x]
            for j in range(26):
                ans += counter[x ^ (1 << j)]
            counter[x] += 1

        return ans



so = Solution()
print(so.countPalindromePaths(parent = [-1,5,0,5,5,2], s = "xsbcqq"))  # 7
print(so.countPalindromePaths(parent = [-1,0,0], s = "aca"))  # 2
print(so.countPalindromePaths(parent = [-1,0,0,1,1,2], s = "acaabc"))  # 8

