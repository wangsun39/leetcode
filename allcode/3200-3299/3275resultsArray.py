# 有一个无限大的二维平面。
#
# 给你一个正整数 k ，同时给你一个二维数组 queries ，包含一系列查询：
#
# queries[i] = [x, y] ：在平面上坐标 (x, y) 处建一个障碍物，数据保证之前的查询 不会 在这个坐标处建立任何障碍物。
# 每次查询后，你需要找到离原点第 k 近 障碍物到原点的 距离 。
#
# 请你返回一个整数数组 results ，其中 results[i] 表示建立第 i 个障碍物以后，离原地第 k 近障碍物距离原点的距离。如果少于 k 个障碍物，results[i] == -1 。
#
# 注意，一开始 没有 任何障碍物。
#
# 坐标在 (x, y) 处的点距离原点的距离定义为 |x| + |y| 。
#
#
#
# 示例 1：
#
# 输入：queries = [[1,2],[3,4],[2,3],[-3,0]], k = 2
#
# 输出：[-1,7,5,3]
#
# 解释：
#
# 最初，不存在障碍物。
#
# queries[0] 之后，少于 2 个障碍物。
# queries[1] 之后， 两个障碍物距离原点的距离分别为 3 和 7 。
# queries[2] 之后，障碍物距离原点的距离分别为 3 ，5 和 7 。
# queries[3] 之后，障碍物距离原点的距离分别为 3，3，5 和 7 。
# 示例 2：
#
# 输入：queries = [[5,5],[4,4],[3,3]], k = 1
#
# 输出：[10,8,6]
#
# 解释：
#
# queries[0] 之后，只有一个障碍物，距离原点距离为 10 。
# queries[1] 之后，障碍物距离原点距离分别为 8 和 10 。
# queries[2] 之后，障碍物距离原点的距离分别为 6， 8 和10 。
#
#
# 提示：
#
# 1 <= queries.length <= 2 * 105
# 所有 queries[i] 互不相同。
# -109 <= queries[i][0], queries[i][1] <= 109
# 1 <= k <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        sl = SortedList()
        ans = []
        for x, y in queries:
            v = abs(x) + abs(y)
            sl.add(v)
            if len(sl) < k:
                ans.append(-1)
            else:
                ans.append(sl[k - 1])
        return ans


so = Solution()
print(so.resultsArray(queries = [[1,2],[3,4],[2,3],[-3,0]], k = 2))
print(so.resultsArray(queries = [[5,5],[4,4],[3,3]], k = 1))
print(so.resultsArray(queries = [[1,2],[3,4],[2,3],[-3,0]], k = 2))




