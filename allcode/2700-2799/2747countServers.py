# 给你一个整数 n ，表示服务器的总数目，再给你一个下标从 0 开始的 二维 整数数组 logs ，其中 logs[i] = [server_id, time] 表示 id 为 server_id 的服务器在 time 时收到了一个请求。
#
# 同时给你一个整数 x 和一个下标从 0 开始的整数数组 queries  。
#
# 请你返回一个长度等于 queries.length 的数组 arr ，其中 arr[i] 表示在时间区间 [queries[i] - x, queries[i]] 内没有收到请求的服务器数目。
#
# 注意时间区间是个闭区间。
#
#
#
# 示例 1：
#
# 输入：n = 3, logs = [[1,3],[2,6],[1,5]], x = 5, queries = [10,11]
# 输出：[1,2]
# 解释：
# 对于 queries[0]：id 为 1 和 2 的服务器在区间 [5, 10] 内收到了请求，所以只有服务器 3 没有收到请求。
# 对于 queries[1]：id 为 2 的服务器在区间 [6,11] 内收到了请求，所以 id 为 1 和 3 的服务器在这个时间段内没有收到请求。
# 示例 2：
#
# 输入：n = 3, logs = [[2,4],[2,1],[1,2],[3,1]], x = 2, queries = [3,4]
# 输出：[0,1]
# 解释：
# 对于 queries[0]：区间 [1, 3] 内所有服务器都收到了请求。
# 对于 queries[1]：只有 id 为 3 的服务器在区间 [2,4] 内没有收到请求。
#
#
# 提示：
#
# 1 <= n <= 105
# 1 <= logs.length <= 105
# 1 <= queries.length <= 105
# logs[i].length == 2
# 1 <= logs[i][0] <= n
# 1 <= logs[i][1] <= 106
# 1 <= x <= 105
# x < queries[i] <= 106

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        nq = len(queries)
        nl = len(logs)
        ans = [0] * nq
        logs.sort(key=lambda x:x[1])
        queries = [[i, x] for i, x in enumerate(queries)]
        queries.sort(key=lambda x:x[1])
        ss = {}
        tt = defaultdict(set)

        l = r = 0
        for i, q in queries:
            left, right = q - x, q
            while r < nl and logs[r][1] <= right:
                if logs[r][0] in ss:
                    ss[logs[r][0]] += 1
                else:
                    ss[logs[r][0]] = 1
                tt[logs[r][1]].add(logs[r][0])
                r += 1
            while l < nl and logs[l][1] < left:
                if l == 0 or logs[l][1] != logs[l - 1][1]:
                    ll = list(tt[logs[l][1]])
                    # print(ss, logs[l][1], ll)
                    for xx in ll:
                        ss[xx] -= 1
                        if ss[xx] == 0:
                            del(ss[xx])
                l += 1
            ans[i] = n - len(ss)
        return ans


so = Solution()
print(so.countServers(n = 3, logs = [[1,3],[2,6],[1,5]], x = 5, queries = [10,11]))
print(so.countServers(n = 3, logs = [[2,4],[2,1],[1,2],[3,1]], x = 2, queries = [3,4]))




