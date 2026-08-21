# 给你一个整数 n 表示一栋建筑的楼层数，楼层编号从 0 到 n - 1 。
#
# 同时给你一个整数 start ，表示电梯的起始楼层，以及一个整数数组 requests ，其中 requests[i] 是电梯需要到达的楼层。requests 中的所有楼层都是 互不相同 的。
#
# 在时间 0 ，电梯在楼层 start ，所有请求都是 同时 发出的。
#
# 在所有请求被处理完之前的每一秒钟，电梯 恰好 移动一层，可以是 向上 也可以是 向下 。当电梯到达请求的楼层时，该请求会被 立即 处理。如果 start 出现在 requests 中，则该请求在时间 0 被处理。
#
# 对于每个未被处理的请求，每一秒钟你会受到 1 点惩罚。等价地说，在时间 t 处理一个请求，它对总惩罚的贡献是 t 。
#
# 返回处理所有请求所需的 最小 总惩罚。
#
#
#
# 示例 1：
#
# 输入： n = 6, start = 4, requests = [1,5]
#
# 输出： 6
#
# 解释：
#
# 从楼层 4（start）移动到楼层 5 需要 1 秒。楼层 5 的惩罚是 1 。
# 从楼层 5 移动到楼层 1 需要 4 秒。楼层 1 的惩罚是 5 。
# 因此，总惩罚是 1 + 5 = 6 。
#
# 示例 2：
#
# 输入： n = 8, start = 3, requests = [3,7,1]
#
# 输出： 10
#
# 解释：
#
# 楼层 3（start）会被立即处理。楼层 3 的惩罚是 0 。
# 从楼层 3 移动到楼层 1 需要 2 秒。楼层 1 的惩罚是 2 。
# 从楼层 1 移动到楼层 7 需要 6 秒。楼层 7 的惩罚是 8 。
# 因此，总惩罚是 0 + 2 + 8 = 10 。
#
# 示例 3：
#
# 输入： n = 10, start = 5, requests = [0,2,9]
#
# 输出： 22
#
# 解释：
#
# 从楼层 5（start）移动到楼层 2 需要 3 秒。楼层 2 的惩罚是 3 。
# 从楼层 2 移动到楼层 0 需要 2 秒。楼层 0 的惩罚是 5 。
# 从楼层 0 移动到楼层 9 需要 9 秒。楼层 9 的惩罚是 14 。
# 因此，总惩罚是 3 + 5 + 14 = 22 。
#
#
#
# 提示：
#
# 1 <= n <= 109
# 1 <= requests.length <= 1500
# 0 <= start, requests[i] <= n - 1
# requests 中的所有值都是 互不相同 的。

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a


class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[int]) -> int:
        requests.sort()
        m = len(requests)

        @cache
        def dfs(l, r, flg):
            # 完成区间[l, r]，且在l或r之一的位置上
            # flg == 0 表示当前在左端点，否则在右端点
            # 返回值，之前总的惩罚值，包括，未到达的点的惩罚
            cnt = m - (r - l + 1)  # 排除区间[l, r]，剩余的点
            if l == r:
                return abs(start - requests[l]) * m

            # 一个小优化，不能过不了
            # 当所有已处理的点都在start一侧时，只需要一趟就是最优路径
            if requests[l] >= start:
                if flg == 0: return inf
                return dfs(l, r - 1, flg) + (requests[r] - requests[r - 1]) * (cnt + 1)
            if requests[r] <= start:
                if flg == 1: return inf
                return dfs(l + 1, r, flg) + (requests[l + 1] - requests[l]) * (cnt + 1)

            if flg == 0:
                # 逆推，最后到达l
                r1 = dfs(l + 1, r, 0) + (requests[l + 1] - requests[l]) * (cnt + 1)
                r2 = dfs(l + 1, r, 1) + (requests[r] - requests[l]) * (cnt + 1)
            else:
                # 逆推，最后到达r
                r1 = dfs(l, r - 1, 1) + (requests[r] - requests[r - 1]) * (cnt + 1)
                r2 = dfs(l, r - 1, 0) + (requests[r] - requests[l]) * (cnt + 1)
            return MIN(r1, r2)

        r1, r2 = dfs(0, m - 1, 0), dfs(0, m - 1, 1)
        ans = MIN(r1, r2)
        dfs.cache_clear()
        return ans




so = Solution()
print(so.elevatorRequests(n = 6, start = 4, requests = [1,5]))



