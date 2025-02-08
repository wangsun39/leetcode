# 给你一个下标从 0 开始的正整数数组 heights ，其中 heights[i] 表示第 i 栋建筑的高度。
#
# 如果一个人在建筑 i ，且存在 i < j 的建筑 j 满足 heights[i] < heights[j] ，那么这个人可以移动到建筑 j 。
#
# 给你另外一个数组 queries ，其中 queries[i] = [ai, bi] 。第 i 个查询中，Alice 在建筑 ai ，Bob 在建筑 bi 。
#
# 请你能返回一个数组 ans ，其中 ans[i] 是第 i 个查询中，Alice 和 Bob 可以相遇的 最左边的建筑 。如果对于查询 i ，Alice 和 Bob 不能相遇，令 ans[i] 为 -1 。
#
#
#
# 示例 1：
#
# 输入：heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
# 输出：[2,5,-1,5,2]
# 解释：第一个查询中，Alice 和 Bob 可以移动到建筑 2 ，因为 heights[0] < heights[2] 且 heights[1] < heights[2] 。
# 第二个查询中，Alice 和 Bob 可以移动到建筑 5 ，因为 heights[0] < heights[5] 且 heights[3] < heights[5] 。
# 第三个查询中，Alice 无法与 Bob 相遇，因为 Alice 不能移动到任何其他建筑。
# 第四个查询中，Alice 和 Bob 可以移动到建筑 5 ，因为 heights[3] < heights[5] 且 heights[4] < heights[5] 。
# 第五个查询中，Alice 和 Bob 已经在同一栋建筑中。
# 对于 ans[i] != -1 ，ans[i] 是 Alice 和 Bob 可以相遇的建筑中最左边建筑的下标。
# 对于 ans[i] == -1 ，不存在 Alice 和 Bob 可以相遇的建筑。
# 示例 2：
#
# 输入：heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]
# 输出：[7,6,-1,4,6]
# 解释：第一个查询中，Alice 可以直接移动到 Bob 的建筑，因为 heights[0] < heights[7] 。
# 第二个查询中，Alice 和 Bob 可以移动到建筑 6 ，因为 heights[3] < heights[6] 且 heights[5] < heights[6] 。
# 第三个查询中，Alice 无法与 Bob 相遇，因为 Bob 不能移动到任何其他建筑。
# 第四个查询中，Alice 和 Bob 可以移动到建筑 4 ，因为 heights[3] < heights[4] 且 heights[0] < heights[4] 。
# 第五个查询中，Alice 可以直接移动到 Bob 的建筑，因为 heights[1] < heights[6] 。
# 对于 ans[i] != -1 ，ans[i] 是 Alice 和 Bob 可以相遇的建筑中最左边建筑的下标。
# 对于 ans[i] == -1 ，不存在 Alice 和 Bob 可以相遇的建筑。
#
#
# 提示：
#
# 1 <= heights.length <= 5 * 104
# 1 <= heights[i] <= 109
# 1 <= queries.length <= 5 * 104
# queries[i] = [ai, bi]
# 0 <= ai, bi <= heights.length - 1

from leetcode.allcode.competition.mypackage import *

class Solution1:
    def leftmostBuildingQueries1(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # 逆序处理
        queries = [sorted(x) for x in queries]
        n = len(heights)
        m = len(queries)
        ans = [-1] * m
        dq = deque()  # [heights[i], i]  单调减的栈
        pos = n - 1
        for i, (idx, idy) in sorted(enumerate(queries), key=lambda x: max(x[1]), reverse=True):
            if heights[idx] < heights[idy] or idx == idy:
                ans[i] = idy
                continue
            while idy < pos:  # 把idy 后侧的点，构造一个单调减的栈，用于查找后侧第一个比idx还大的点的位置
                while dq and dq[0][0] <= heights[pos]:
                    dq.popleft()
                dq.appendleft([heights[pos], pos])
                pos -= 1
            # print(stack)
            p = bisect_left(dq, [heights[idx], n])  # 单调栈上二分
            if p == len(dq):
                ans[i] = -1
            else:
                ans[i] = dq[p][1]
        return ans

    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # 2024/8/11 顺序处理，最小堆
        queries = [[x, y] if x <= y else [y, x] for x, y in queries]
        n = len(heights)
        m = len(queries)
        ans = [-1] * m

        hp = []
        cur = 0
        for i, (idx, idy) in sorted(enumerate(queries), key=lambda x: max(x[1])):
            hx, hy = heights[idx], heights[idy]
            solve = False
            if idx == idy or hx < hy:
                ans[i] = idy
                solve = True

            while cur < idy:
                while hp and hp[0][0] < heights[cur]:
                    mn_h, mn_i = heappop(hp)
                    ans[mn_i] = cur
                cur += 1
            if not solve:
                heappush(hp, [heights[idx], i])

        while cur < n:
            while hp and hp[0][0] < heights[cur]:
                mn_h, mn_i = heappop(hp)
                ans[mn_i] = cur
            cur += 1

        return ans


# 2025/2/7 线段树上二分
class STree2:
    # 非动态开点，单点更新，区间查询
    def __init__(self, n: int):
        # self.n = n
        self.max = [0] * (2 << n.bit_length())  # 相比 4n 空间更小

    # 线段树：把下标 i 上的元素值增加 val，单点更新
    # o 是当前区间对应的下标，[l, r]当前区间的范围
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

    # 线段树：返回区间 [L,R] 内最左侧的一个大于val的下标
    # 线段树上二分
    def query_left(self, o: int, l: int, r: int, L: int, val: int) -> int:
        if self.max[o] <= val: return -1
        if l == r:
            return l
        # res = 0
        m = (l + r) // 2
        if L <= m:
            if (res := self.query_left(o * 2, l, m, L, val)) > 0:
                return res
        return self.query_left(o * 2 + 1, m + 1, r, L, val)

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        st = STree2(n)
        for i, x in enumerate(heights):
            st.update(1, 0, n - 1, i, x)
        ans = []

        for a, b in queries:
            if a > b: a, b = b, a
            if a == b or heights[a] < heights[b]:
                ans.append(b)
                continue
            ans.append(st.query_left(1, 0, n - 1, b + 1, heights[a]))
        return ans



so = Solution()
print(so.leftmostBuildingQueries(heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]))  # [2,5,-1,5,2]
print(so.leftmostBuildingQueries(heights = [1,2,1,2,1,2], queries = [[0,2]]))  # [3]
print(so.leftmostBuildingQueries(heights = [4,1,2,3,5], queries = [[0,1]]))  # [4]
print(so.leftmostBuildingQueries(heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]))  # [7,6,-1,4,6]
print(so.leftmostBuildingQueries(heights = [1,2,1,2,1,2], queries = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],[5,0],[5,1],[5,2],[5,3],[5,4],[5,5]]))





