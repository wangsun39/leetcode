# 给你 k 枚相同的鸡蛋，并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。
#
# 已知存在楼层 f ，满足 0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。
#
# 每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下（满足 1 <= x <= n）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。
#
# 请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？
#
#
# 示例 1：
#
# 输入：k = 1, n = 2
# 输出：2
# 解释：
# 鸡蛋从 1 楼掉落。如果它碎了，肯定能得出 f = 0 。
# 否则，鸡蛋从 2 楼掉落。如果它碎了，肯定能得出 f = 1 。
# 如果它没碎，那么肯定能得出 f = 2 。
# 因此，在最坏的情况下我们需要移动 2 次以确定 f 是多少。
# 示例 2：
#
# 输入：k = 2, n = 6
# 输出：3
# 示例 3：
#
# 输入：k = 3, n = 14
# 输出：4
#
#
# 提示：
#
# 1 <= k <= 100
# 1 <= n <= 104

from leetcode.allcode.competition.mypackage import *

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:

        @cache
        def dfs(kk, nn):  # 考虑子问题
            if kk == 1: return nn
            if nn <= 2: return nn

            # 正常的递归
            # res = inf
            # for i in range(1, nn + 1):
            #     res = min(res, max(dfs(kk - 1, i - 1), dfs(kk, nn - i)) + 1)

            # dfs(kk, nn) 当kk相同时，是nn的单调增函数
            # 二分，去寻找最大的i，使得 dfs(kk - 1, i - 1) <= dfs(kk, nn - i) 的 i
            lo, hi = 1, n
            while lo < hi - 1:
                mid = (lo + hi) // 2
                if dfs(kk - 1, mid - 1) <= dfs(kk, nn - mid):
                    lo = mid
                else:
                    hi = mid

            # 此时i = lo时， dfs(kk - 1, i - 1) <= dfs(kk, nn - i) 并且 i = lo + 1时, dfs(kk - 1, i - 1) >= dfs(kk, nn - i)
            # 取两者最大值的最小值

            return min(dfs(kk - 1, lo), dfs(kk, nn - lo)) + 1

        return dfs(k, n)


so = Solution()
print(so.superEggDrop(k = 2, n = 4))  # 3
print(so.superEggDrop(k = 2, n = 6))  # 3

