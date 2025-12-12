# 小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 leaves， 字符串 leaves 仅包含小写字符 r 和 y， 其中字符 r 表示一片红叶，字符 y 表示一片黄叶。 出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。每部分树叶数量可以不相等，但均需大于等于 1。每次调整操作，小扣可以将一片红叶替换成黄叶或者将一片黄叶替换成红叶。请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。
#
# 示例 1：
#
# 输入：leaves = "rrryyyrryyyrr"
#
# 输出：2
#
# 解释：调整两次，将中间的两片红叶替换成黄叶，得到 "rrryyyyyyyyrr"
#
# 示例 2：
#
# 输入：leaves = "ryr"
#
# 输出：0
#
# 解释：已符合要求，不需要额外操作
#
# 提示：
#
# 3 <= leaves.length <= 10^5
# leaves 中只包含字符 'r' 和字符 'y'

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        cr = 0
        suf = [0] * n  # 把后缀变成全r需要的操作次
        for i in range(n - 1, -1, -1):
            if leaves[i] == 'y':
                cr += 1
            suf[i] = cr

        ans = n
        # 处理前缀形成 rrryyy 形式的最小操作次数  次数=min(cy[j]+(cr[i]-cr[j]))  对固定的i，对所有的j<i取最小
        cy = cr = 0
        if leaves[0] == 'y':
            cy += 1
        else:
            cr += 1
        mx_diff = cr - cy  # 记录最大的 cr[j]-cy[j]
        for i, x in enumerate(leaves[1: -1], 1):
            if x == 'r':
                cr += 1
            ans = min(ans, cr - mx_diff + suf[i + 1])
            mx_diff = max(mx_diff, cr - cy)
            if x == 'y':
                cy += 1
        return ans


so = Solution()
print(so.minimumOperations(leaves = "ryr"))  # 0
print(so.minimumOperations(leaves = "yry"))  # 3
print(so.minimumOperations(leaves = "rrryyyrryyyrr"))  # 2

