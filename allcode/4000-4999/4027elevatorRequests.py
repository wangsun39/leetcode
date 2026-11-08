# 给你一个整数 n 表示一栋建筑的楼层数，楼层编号从 0 到 n - 1 。
#
# 同时给你一个整数 start ，表示电梯的起始楼层，以及一个二维整数数组 requests ，其中 requests[i] = [arrivali, floori] 表示在时间 arrivali 发出了一个前往楼层 floori 的请求。
#
# 在时间 0 ，电梯在楼层 start 。
#
# 每一秒钟，电梯可以 向上 移动一层、向下 移动一层，或者 停留 在当前楼层。
#
# 一个请求 只能 在其到达时间或之后被处理；从请求到达时起，只要电梯在任意时刻位于该请求对应的楼层，该请求就会被 立即 处理。
#
# 返回处理所有请求所需的 最短 时间。
#
#
#
# 示例 1：
#
# 输入： n = 9, start = 0, requests = [[0,8],[6,5]]
#
# 输出： 9
#
# 解释：
#
# 从楼层 0（start）移动到楼层 5（requests[1][1]）需要 5 秒，在时间 5 到达。由于 requests[1][0] = 6，等待到时间 6 再处理该请求。
# 从楼层 5 移动到楼层 8（requests[0][1]）需要 3 秒，在时间 9 处理该请求。
# 因此，所有请求都在时间 9 被处理完。
#
# 示例 2：
#
# 输入： n = 8, start = 5, requests = [[1,7],[7,3]]
#
# 输出： 7
#
# 解释：
#
# 从楼层 5（start）移动到楼层 7（requests[0][1]）需要 2 秒，在时间 2 到达。由于 requests[0][0] = 1 已经过去，因此楼层 7 的请求在时间 2 被处理。
# 从楼层 7 移动到楼层 3（requests[1][1]）需要 4 秒，在时间 6 到达。由于 requests[1][0] = 7，等待到时间 7 。
# 因此，所有请求都在时间 7 被处理完。
#
# 示例 3：
#
# 输入： n = 7, start = 3, requests = [[0,5],[0,1],[6,3]]
#
# 输出： 8
#
# 解释：
#
# 从楼层 3（start）移动到楼层 5（requests[0][1]）需要 2 秒，在时间 2 处理该请求。
# 从楼层 5 移动到楼层 1（requests[1][1]）需要 4 秒，在时间 6 处理该请求。
# 从楼层 1 移动到楼层 3（requests[2][1]）需要 2 秒，在时间 8 到达。该请求在 requests[2][0] = 6 时到达，因此楼层 3 的请求在时间 8 被处理。
# 因此，所有请求都在时间 8 被处理完。
#
#
#
# 提示：
#
# 1 <= n <= 109
# 1 <= requests.length <= 16
# requests[i] == [arrivali, floori]
# 0 <= arrivali <= 109
# 0 <= start, floori <= n - 1

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a


class Solution:
    def elevatorRequests1(self, n: int, start: int, requests: list[list[int]]) -> int:
        m = len(requests)
        # 这样的状态设计是不能通过用例的，复杂多了一个t的参数
        @cache
        def dfs(mask, pos, t):
            # 当前t时刻，在 req[pos][1] 位置，剩余未处理的 req 掩码 mask，返回处理完剩余的请求所需要的最小时间
            nonlocal ans
            if t < requests[pos][0]:
                t = requests[pos][0]
            # res = inf
            mask ^= (1 << pos)
            if mask == 0:
                ans = MIN(ans, t)
                return
            for i in range(m):
                if mask & (1 << i):
                    t1 = t + abs(requests[i][1] - requests[pos][1])
                    dfs(mask, i, t1)
                    # res = MIN(res, )
            return

        ans = inf
        al = (1 << m) - 1
        for i in range(m):
            dfs(al, i, abs(start - requests[i][1]))

        dfs.cache_clear()
        return ans

    def elevatorRequests(self, n: int, start: int, requests: list[list[int]]) -> int:
        m = len(requests)


        @cache
        def dfs(mask, pos):
            # 当前在 req[pos][1] 位置，已处理的 req 掩码 mask，返回到达当前这个位置的最早时间
            if mask.bit_count() == 1:
                t1 = abs(requests[pos][1] - start)
                return MAX(t1, requests[pos][0])
            pre = mask ^ (1 << pos)
            res = inf
            for i in range(m):
                if pre & (1 << i):
                    # 从 i 转移到 pos
                    t = dfs(pre, i) + abs(requests[i][1] - requests[pos][1])
                    if t < requests[pos][0]:
                        res = MIN(res, requests[pos][0])
                    else:
                        res = MIN(res, t)
            return res

        ans = inf
        al = (1 << m) - 1
        for i in range(m):
            ans = MIN(ans, dfs(al, i))

        dfs.cache_clear()
        return ans



so = Solution()
print(so.elevatorRequests(n = 9, start = 0, requests = [[0,8],[6,5]]))



