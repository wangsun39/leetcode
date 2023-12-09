# 如果整数  x 满足：对于每个数位 d ，这个数位 恰好 在 x 中出现 d 次。那么整数 x 就是一个 数值平衡数 。
#
# 给你一个整数 n ，请你返回 严格大于 n 的 最小数值平衡数 。
#
#
#
# 示例 1：
#
# 输入：n = 1
# 输出：22
# 解释：
# 22 是一个数值平衡数，因为：
# - 数字 2 出现 2 次
# 这也是严格大于 1 的最小数值平衡数。
# 示例 2：
#
# 输入：n = 1000
# 输出：1333
# 解释：
# 1333 是一个数值平衡数，因为：
# - 数字 1 出现 1 次。
# - 数字 3 出现 3 次。
# 这也是严格大于 1000 的最小数值平衡数。
# 注意，1022 不能作为本输入的答案，因为数字 0 的出现次数超过了 0 。
# 示例 3：
#
# 输入：n = 3000
# 输出：3133
# 解释：
# 3133 是一个数值平衡数，因为：
# - 数字 1 出现 1 次。
# - 数字 3 出现 3 次。
# 这也是严格大于 3000 的最小数值平衡数。
#
#
# 提示：
#
# 0 <= n <= 106
import itertools

from leetcode.allcode.competition.mypackage import *

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        group = [['1'], ['22'], ['122', '333'], ['1333', '4444'], ['14444','22333','55555'],['122333','155555', '224444','666666'], ['1224444']]
        l = len(str(n))
        if n >= 10 ** 6:
            return int(group[-1][0])
        if n >= int(group[l - 1][-1]):
            return int(group[l][0])
        ans = inf
        for g in group[l - 1]:
            if n >= int(g[::-1]):
                continue
            perms = itertools.permutations(g)
            perms = [''.join(perm) for perm in perms]
            perms.sort()
            for p in perms:
                if n < int(p):
                    ans = min(ans, int(p))
        return ans


so = Solution()
print(so.nextBeautifulNumber(16407))
print(so.nextBeautifulNumber(1000))
print(so.nextBeautifulNumber(1))
print(so.nextBeautifulNumber(3000))

