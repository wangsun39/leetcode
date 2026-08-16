# 给你一个长度为 n 的整数数组 nums 和一个二维整数数组 queries。
#
# 如果满足以下条件，子数组 nums[i..j] 被称为 峰值子数组：
#
# 其长度 至少 为 3。
# 存在一个下标 k 使得 i < k < j 且：
# nums[k] > nums[k - 1]
# nums[k] > nums[k + 1]
# 你需要处理以下两种类型的查询：
#
# [1, li, ri]：计算完全包含在 nums[li..ri] 中的 峰值子数组 的数量。
# [2, indexi, vali]：将 nums[indexi] 更新为 vali。此更新适用于所有后续查询。
# 返回一个数组 answer，其中 answer[i] 是按出现顺序排列的第 i 个类型 1 查询的答案。
#
# 子数组 是数组中连续的 非空 元素序列。
#
#
#
# 示例 1：
#
# 输入： nums = [1,3,2,4], queries = [[1,0,3],[2,1,1],[1,0,3]]
#
# 输出： [2,0]
#
# 解释：
#
# 查询 [1, 0, 3]：
# [1, 3, 2]：选择 k = 1。则 nums[k] = 3，nums[k - 1] = 1，且 nums[k + 1] = 2。因为 3 > 1 且 3 > 2，这是一个峰值子数组。
# [1, 3, 2, 4]：选择 k = 1。则 nums[k] = 3，nums[k - 1] = 1，且 nums[k + 1] = 2。因为 3 > 1 且 3 > 2，这是一个峰值子数组。
# 查询 [2, 1, 1]：将 nums[1] 更新为 1。数组变为 [1, 1, 2, 4]。
# 查询 [1, 0, 3]：现在没有峰值子数组。
# 因此，answer = [2, 0]。
# 示例 2：
#
# 输入： nums = [9,8,9,8], queries = [[1,1,3],[2,2,1],[1,0,2]]
#
# 输出： [1,0]
#
# 解释：
#
# 查询 [1, 1, 3]：
# nums[1..3] = [8, 9, 8]：选择 k = 2。则 nums[k] = 9，nums[k - 1] = 8，且 nums[k + 1] = 8。因为 9 > 8 且 9 > 8，这是一个峰值子数组。
# 查询 [2, 2, 1]：将 nums[2] 更新为 1。数组变为 [9, 8, 1, 8]。
# 查询 [1, 0, 2]：没有峰值子数组。
# 因此，answer = [1, 0]。
# 示例 3：
#
# 输入： nums = [3,6,2,7,1], queries = [[1,1,3],[2,3,0],[1,0,4]]
#
# 输出： [0,3]
#
# 解释：
#
# 查询 [1, 1, 3]：唯一长度至少为 3 的子数组是 [6, 2, 7]。其唯一可能的峰值下标是 k = 2，但 nums[2] = 2 小于 nums[1] = 6 和 nums[3] = 7，因此它不是一个峰值子数组。
# 查询 [2, 3, 0]：将 nums[3] 更新为 0。数组变为 [3, 6, 2, 0, 1]。
# 查询 [1, 0, 4]：
# [3, 6, 2]：选择 k = 1。则 nums[k] = 6，nums[k - 1] = 3，且 nums[k + 1] = 2。因为 6 > 3 且 6 > 2，这是一个峰值子数组。
# [3, 6, 2, 0]：选择 k = 1。则 nums[k] = 6，nums[k - 1] = 3，且 nums[k + 1] = 2。因为 6 > 3 且 6 > 2，这是一个峰值子数组。
# [3, 6, 2, 0, 1]：选择 k = 1。则 nums[k] = 6，nums[k - 1] = 3，且 nums[k + 1] = 2。因为 6 > 3 且 6 > 2，这是一个峰值子数组。
# 因此，answer = [0, 3]。
#
#
# 提示：
#
# 3 <= n == nums.length <= 105
# 0 <= nums[i] <= 105
# 1 <= queries.length <= 105
# queries[i] = [1, li, ri] 或 queries[i] = [2, indexi, vali]
# 0 <= li < ri <= n - 1
# 0 <= indexi <= n - 1
# 0 <= vali <= 105

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class SegmentTree:
    def __init__(self, arr, default=0):
        # 线段树维护一个长为 n 的数组（下标从 0 到 n-1）
        # arr 可以是 list 或者 int
        # 如果 arr 是 int，视作数组大小，默认值为 default
        if isinstance(arr, int):
            arr = [default] * arr
        self._arr = arr[:]
        n = len(arr)
        m = (2 << (n - 1).bit_length())
        self._n = n
        # self._tree = [0] * m
        self._first = [-1] * m   # 区间内第一个峰值子数组的最后一个元素下标
        self._last = [-1] * m  # 区间内最后一个峰值子数组的第一个元素下标
        self._count = [0] * m  # 区间内峰值子数组个数
        self._build(arr, 1, 0, n - 1)

    # 合并两个 val
    def _merge_val(self, l_cnt, l_first, l_last, r_cnt, r_first, r_last, ll, lr, rr) -> List[int]:
        # **根据题目修改**
        # 返回三个值：
        # 合并区间 [ql, qr] 中的内峰值子数组个数，
        # 区间内第一个峰值子数组的最后一个元素下标，
        # 区间内最后一个峰值子数组的第一个元素下标
        # l_cnt, l_first, l_last 是左子节点的 count/first/last 值
        # r_cnt, r_first, r_last 是右子节点的 count/first/last 值
        # ll, lr, rr  左右区间的左右端点
        if rr - ll + 1 < 3:
            return [0, -1, -1]
        rl = lr + 1
        mid_l = mid_r = -1
        if rl + 1 <= rr and self._arr[lr] < self._arr[rl] > self._arr[rl + 1]:
            mid_l = lr
            mid_r = rl + 1
        elif self._arr[lr - 1] < self._arr[lr] > self._arr[rl]:
            mid_l = lr - 1
            mid_r = rl

        if l_last == r_first == mid_l == -1:
            return [0, -1, -1]

        if l_last == r_first == -1:
            return [(mid_l - ll + 1) * (rr - mid_r + 1), mid_r, mid_l]

        if l_last == -1:
            r1 = (lr - ll + 1) * (rr - r_first + 1)
            if mid_l == -1:
                return [r1 + r_cnt, r_first, r_last]
            else:
                r2 = (r_first - mid_r) * (mid_l - ll + 1)
                return [r1 + r2 + r_cnt, mid_r, r_last]
        if r_first == -1:
            r1 = (l_last - ll + 1) * (rr - rl + 1)
            if mid_l == -1:
                return [r1 + l_cnt, l_first, l_last]
            else:
                r2 = (mid_l - l_last) * (rr - mid_r + 1)
                return [r1 + r2 + l_cnt, l_first, mid_l]

        r1 = (l_last - ll + 1) * (rr - rl + 1)
        r2 = (lr - l_last) * (rr - r_first + 1)
        if mid_l == -1:
            return [l_cnt + r_cnt + r1 + r2, l_first, r_last]
        r3 = (mid_l - l_last) * (r_first - mid_r)
        return [l_cnt + r_cnt + r1 + r2 + r3, l_first, r_last]

    # 合并左右儿子的 val 到当前节点的 val
    def _maintain(self, node: int, l, r) -> None:
        m = (l + r) // 2
        self._count[node], self._first[node], self._last[node] = self._merge_val(self._count[node * 2], self._first[node * 2], self._last[node * 2],
                                            self._count[node * 2 + 1], self._first[node * 2 + 1], self._last[node * 2 + 1],
                                            l, m, r)

    # 用 a 初始化线段树
    # 时间复杂度 O(n)
    def _build(self, a: List[int], node: int, l: int, r: int) -> None:
        if l == r:  # 叶子
            # self._count[node] = a[l]  # 初始化叶节点的值
            return
        m = (l + r) // 2
        self._build(a, node * 2, l, m)  # 初始化左子树
        self._build(a, node * 2 + 1, m + 1, r)  # 初始化右子树
        self._maintain(node, l, r)

    def _update(self, node: int, l: int, r: int, i: int, val: int) -> None:
        if l == r:  # 叶子（到达目标）
            # 如果想直接替换的话，可以写 self._count[node] = val
            # self._count[node] = self._merge_val(self._count[node], val)
            self._arr[i] = val
            return
        m = (l + r) // 2
        if i <= m:  # i 在左子树
            self._update(node * 2, l, m, i, val)
        else:  # i 在右子树
            self._update(node * 2 + 1, m + 1, r, i, val)
        self._maintain(node, l, r)

    def _query(self, node: int, l: int, r: int, ql: int, qr: int) -> List[int]:
        # 返回三个值：
        # 查询区间 [ql, qr] 中的内峰值子数组个数，
        # 区间内第一个峰值子数组的最后一个元素下标，
        # 区间内最后一个峰值子数组的第一个元素下标
        if ql <= l and r <= qr:  # 当前子树完全在 [ql, qr] 内
            return [self._count[node], self._first[node], self._last[node]]
        m = (l + r) // 2
        if qr <= m:  # [ql, qr] 在左子树
            return self._query(node * 2, l, m, ql, qr)
        if ql > m:  # [ql, qr] 在右子树
            return self._query(node * 2 + 1, m + 1, r, ql, qr)
        l_c, l_f, l_l = self._query(node * 2, l, m, ql, qr)
        r_c, r_f, r_l = self._query(node * 2 + 1, m + 1, r, ql, qr)
        return self._merge_val(l_c, l_f, l_l, r_c, r_f, r_l, MAX(ql, l), m, MIN(qr, r))

    # 更新 a[i] 为 _merge_val(a[i], val)
    # 时间复杂度 O(log n)
    def update(self, i: int, val: int) -> None:
        self._update(1, 0, self._n - 1, i, val)

    # 返回用 _merge_val 合并所有 a[i] 的计算结果，其中 i 在闭区间 [ql, qr] 中
    # 时间复杂度 O(log n)
    def query(self, ql: int, qr: int) -> int:
        return self._query(1, 0, self._n - 1, ql, qr)[0]



class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        st = SegmentTree(nums)
        ans = []
        for q, l, r in queries:
            if q == 1:
                ans.append(st.query(l, r))
            else:
                st.update(l, r)
        return ans


so = Solution()
print(so.countOfPeaks(nums = [7,15,20,14,2,5,12,0,15,18], queries = [[1,0,6],[1,5,6],[1,6,9]]))
print(so.countOfPeaks(nums = [13,9,1,6,12,5], queries = [[1,1,5],[2,0,3]]))
print(so.countOfPeaks(nums = [3,6,2,7,1], queries = [[1,1,3],[1,0,4],[2,3,0]]))
print(so.countOfPeaks(nums = [1,3,2,4], queries = [[1,0,3],[2,1,1],[1,0,3]]))



