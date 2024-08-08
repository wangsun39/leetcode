# 给你一个整数 n 和一个二维整数数组 queries。
#
# 有 n 个城市，编号从 0 到 n - 1。初始时，每个城市 i 都有一条单向道路通往城市 i + 1（ 0 <= i < n - 1）。
#
# queries[i] = [ui, vi] 表示新建一条从城市 ui 到城市 vi 的单向道路。每次查询后，你需要找到从城市 0 到城市 n - 1 的最短路径的长度。
#
# 所有查询中不会存在两个查询都满足 queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1]。
#
# 返回一个数组 answer，对于范围 [0, queries.length - 1] 中的每个 i，answer[i] 是处理完前 i + 1 个查询后，从城市 0 到城市 n - 1 的最短路径的长度。
#
#
#
# 示例 1：
#
# 输入： n = 5, queries = [[2, 4], [0, 2], [0, 4]]
#
# 输出： [3, 2, 1]
#
# 解释：
#
#
#
# 新增一条从 2 到 4 的道路后，从 0 到 4 的最短路径长度为 3。
#
#
#
# 新增一条从 0 到 2 的道路后，从 0 到 4 的最短路径长度为 2。
#
#
#
# 新增一条从 0 到 4 的道路后，从 0 到 4 的最短路径长度为 1。
#
# 示例 2：
#
# 输入： n = 4, queries = [[0, 3], [0, 2]]
#
# 输出： [1, 1]
#
# 解释：
#
#
#
# 新增一条从 0 到 3 的道路后，从 0 到 3 的最短路径长度为 1。
#
#
#
# 新增一条从 0 到 2 的道路后，从 0 到 3 的最短路径长度仍为 1。
#
#
#
# 提示:
#
# 3 <= n <= 105
# 1 <= queries.length <= 105
# queries[i].length == 2
# 0 <= queries[i][0] < queries[i][1] < n
# 1 < queries[i][1] - queries[i][0]
# 查询中不存在重复的道路。
# 不存在两个查询都满足 i != j 且 queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1]。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        rmv = SortedList()
        ans = []
        cur = n - 1
        for x, y in queries:
            if len(rmv) == 0 or x > rmv[-1][1]:
                rmv.add([x, y])
                cur -= (y - x - 1)
                ans.append(cur)
                continue
            p = rmv.bisect_right([x, y])
            if p == 0:
                if rmv[0][0] == x and rmv[0][1] >= y:
                    ans.append(cur)
                    continue
                if rmv[0][0] >= y:
                    rmv.add([x, y])
                    cur -= (y - x - 1)
                    ans.append(cur)
                    continue
            elif rmv[p - 1][1] >= y:
                ans.append(cur)
                continue
            elif rmv[p - 1][0] == x:
                p = p - 1
            # 剩下的情况，就是 [x,y] 包含已有的区间，需要合并掉
            dis0 = 0  # 之前减少的长度
            while p < len(rmv) and rmv[p][1] <= y:
                dis0 += (rmv[p][1] - rmv[p][0] - 1)
                del(rmv[p])
            dis1 = y - x - 1  # 现在减少的长度
            rmv.add([x, y])
            cur -= (dis1 - dis0)
            ans.append(cur)
        return ans


so = Solution()
print(so.shortestDistanceAfterQueries( n = 6, queries = [[3,5],[2,5]]))  # [4,3]
print(so.shortestDistanceAfterQueries( n = 5, queries = [[1,4],[2,4]]))  # [2,2]
print(so.shortestDistanceAfterQueries( n = 5, queries = [[2, 4], [0, 2], [0, 4]]))
print(so.shortestDistanceAfterQueries( n = 4, queries = [[0, 3], [0, 2]]))




