# 有一条无限长的数轴，原点在 0 处，沿着 x 轴 正 方向无限延伸。
#
# 给你一个二维数组 queries ，它包含两种操作：
#
# 操作类型 1 ：queries[i] = [1, x] 。在距离原点 x 处建一个障碍物。数据保证当操作执行的时候，位置 x 处 没有 任何障碍物。
# 操作类型 2 ：queries[i] = [2, x, sz] 。判断在数轴范围 [0, x] 内是否可以放置一个长度为 sz 的物块，这个物块需要 完全 放置在范围 [0, x] 内。如果物块与任何障碍物有重合，那么这个物块 不能 被放置，但物块可以与障碍物刚好接触。注意，你只是进行查询，并 不是 真的放置这个物块。每个查询都是相互独立的。
# 请你返回一个 boolean 数组results ，如果第 i 个操作类型 2 的操作你可以放置物块，那么 results[i] 为 true ，否则为 false 。
#
#
#
# 示例 1：
#
# 输入：queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]
#
# 输出：[false,true,true]
#
# 解释：
#
#
#
# 查询 0 ，在 x = 2 处放置一个障碍物。在 x = 3 之前任何大小不超过 2 的物块都可以被放置。
#
# 示例 2：
#
# 输入：queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]
#
# 输出：[true,true,false]
#
# 解释：
#
#
#
# 查询 0 在 x = 7 处放置一个障碍物。在 x = 7 之前任何大小不超过 7 的物块都可以被放置。
# 查询 2 在 x = 2 处放置一个障碍物。现在，在 x = 7 之前任何大小不超过 5 的物块可以被放置，x = 2 之前任何大小不超过 2 的物块可以被放置。
#
#
# 提示：
#
# 1 <= queries.length <= 15 * 104
# 2 <= queries[i].length <= 3
# 1 <= queries[i][0] <= 2
# 1 <= x, sz <= min(5 * 104, 3 * queries.length)
# 输入保证操作 1 中，x 处不会有障碍物。
# 输入保证至少有一个操作类型 2 。

from leetcode.allcode.competition.mypackage import *

class STree2:
    # 非动态开点，单点更新，区间查询
    def __init__(self, n: int):
        # self.n = n
        self.max = [0] * (2 << n.bit_length())  # 相比 4n 空间更小

    # 线段树：把下标 i 上的元素值增加 val，单点更新
    # o 是当前区间对应的下标，[l, r]当前区间的范围
    # 调用入口update(1,1,n,...) 或 update(1,0,n-1,...) 根据实际需要填写，l和r一般情况可以不用，就标识一个范围，不会产生越界
    def update(self, o: int, l: int, r: int, i: int, val: int) -> None:
        if l == r:
            self.max[o] = val
            return
        m = (l + r) // 2
        if i <= m:
            self.update(o * 2, l, m, i, val)
        else:
            self.update(o * 2 + 1, m + 1, r, i, val)
        self.max[o] = max(self.max[o * 2], self.max[o * 2 + 1])

    # 线段树：返回区间 [L,R] 内的元素和，区间查询最大值
    # 调用入口 query(1,1,n,...) 或 query(1,0,n-1,...)
    def query(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if L <= l and r <= R:
            return self.max[o]
        res = 0
        m = (l + r) // 2
        if L <= m:
            res = max(res, self.query(o * 2, l, m, L, R))
        if R > m:
            res = max(res, self.query(o * 2 + 1, m + 1, r, L, R))
        return res

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        MX = 10 ** 5
        st = STree2(10 ** 5)
        sl = SortedList([0])
        n = len(queries)
        ans = []
        for i in range(n):
            x = queries[i][1]
            p = sl.bisect_left(x)
            if queries[i][0] == 1:
                # 把一个小段的长度，更新到这段右端点对应的下标上，这步是关键
                st.update(1, 0, MX, x, x - sl[p - 1])
                if p < len(sl):
                    st.update(1, 0, MX, sl[p], sl[p] - x)
                sl.add(x)
            else:
                sz = queries[i][2]
                v1 = st.query(1, 0, MX, 0, x)
                v2 = p - sl[p - 1]
                if max(v1, v2) >= sz:
                    ans.append(True)
                else:
                    ans.append(False)
        return ans


so = Solution()
print(so.getResults(queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]))
print(so.getResults(queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]))




