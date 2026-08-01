# 给你一个长度为 n 的整数数组 nums 和一个整数 p。
#
# 如果 nums 的一个 非空子序列 满足以下条件，则称其为 好子序列：
#
# 其长度 严格小于 n。
# 其所有元素的 最大公约数（GCD）恰好等于 p。
# 另给定一个长度为 q 的二维整数数组 queries，其中 queries[i] = [indi, vali] 表示你需要将 nums[indi] 更新为 vali。
#
# 在每次查询更新后，判断当前数组中是否存在 任意一个好子序列。
#
# 返回一个整数，表示使得数组中存在 好子序列 的查询 次数。
#
# 子序列 是指通过删除原序列中的某些元素或不删除任何元素，并且不改变剩余元素相对顺序后得到的序列。
#
# gcd(a, b) 表示 a 和 b 的 最大公约数。
#
#
#
# 示例 1：
#
# 输入： nums = [4,8,12,16], p = 2, queries = [[0,3],[2,6]]
#
# 输出： 1
#
# 解释：
#
# i	[indi, vali]	操作	更新后的 nums	是否存在好子序列
# 0	[0, 3]	将 nums[0] 更新为 3	[3, 8, 12, 16]	否，因为不存在最大公约数恰好为 p = 2 的子序列
# 1	[2, 6]	将 nums[2] 更新为 6	[3, 8, 6, 16]	是，子序列 [8, 6] 的最大公约数恰好为 p = 2
# 因此，答案是 1。
#
# 示例 2：
#
# 输入： nums = [4,5,7,8], p = 3, queries = [[0,6],[1,9],[2,3]]
#
# 输出： 2
#
# 解释：
#
# i	[indi, vali]	操作	更新后的 nums	是否存在好子序列
# 0	[0, 6]	将 nums[0] 更新为 6	[6, 5, 7, 8]	否，因为不存在最大公约数恰好为 p = 3 的子序列
# 1	[1, 9]	将 nums[1] 更新为 9	[6, 9, 7, 8]	是，子序列 [6, 9] 的最大公约数恰好为 p = 3
# 2	[2, 3]	将 nums[2] 更新为 3	[6, 9, 3, 8]	是，子序列 [6, 9, 3] 的最大公约数恰好为 p = 3
# 因此，答案是 2。
#
# 示例 3：
#
# 输入： nums = [5,7,9], p = 2, queries = [[1,4],[2,8]]
#
# 输出： 0
#
# 解释：
#
# i	[indi, vali]	操作	更新后的 nums	是否存在好子序列
# 0	[1, 4]	将 nums[1] 更新为 4	[5, 4, 9]	否，因为不存在最大公约数恰好为 p = 2 的子序列
# 1	[2, 8]	将 nums[2] 更新为 8	[5, 4, 8]	否，因为不存在最大公约数恰好为 p = 2 的子序列
# 因此，答案是 0。
#
#
#
# 提示：
#
# 2 <= n == nums.length <= 5 * 104
# 1 <= nums[i] <= 5 * 104
# 1 <= queries.length <= 5 * 104
# queries[i] = [indi, vali]
# 1 <= vali, p <= 5 * 104
# 0 <= indi <= n - 1

from leetcode.allcode.competition.mypackage import *

class SegmentTree:
    def __init__(self, arr, default=0):
        # 线段树维护一个长为 n 的数组（下标从 0 到 n-1）
        # arr 可以是 list 或者 int
        # 如果 arr 是 int，视作数组大小，默认值为 default
        if isinstance(arr, int):
            arr = [default] * arr
        n = len(arr)
        self._n = n
        self._tree = [0] * (2 << (n - 1).bit_length())
        self._build(arr, 1, 0, n - 1)

    # 合并两个 val
    def _merge_val(self, a: int, b: int) -> int:
        if a == 0:
            return b
        if b == 0:
            return a
        return gcd(a, b)  # **根据题目修改**

    # 合并左右儿子的 val 到当前节点的 val
    def _maintain(self, node: int) -> None:
        self._tree[node] = self._merge_val(self._tree[node * 2], self._tree[node * 2 + 1])

    # 用 a 初始化线段树
    # 时间复杂度 O(n)
    def _build(self, a: List[int], node: int, l: int, r: int) -> None:
        if l == r:  # 叶子
            self._tree[node] = a[l]  # 初始化叶节点的值
            return
        m = (l + r) // 2
        self._build(a, node * 2, l, m)  # 初始化左子树
        self._build(a, node * 2 + 1, m + 1, r)  # 初始化右子树
        self._maintain(node)

    def _update(self, node: int, l: int, r: int, i: int, val: int) -> None:
        if l == r:  # 叶子（到达目标）
            # 如果想直接替换的话，可以写 self._tree[node] = val
            # self._tree[node] = self._merge_val(self._tree[node], val)
            self._tree[node] = val
            return
        m = (l + r) // 2
        if i <= m:  # i 在左子树
            self._update(node * 2, l, m, i, val)
        else:  # i 在右子树
            self._update(node * 2 + 1, m + 1, r, i, val)
        self._maintain(node)

    def _query(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql <= l and r <= qr:  # 当前子树完全在 [ql, qr] 内
            return self._tree[node]
        m = (l + r) // 2
        if qr <= m:  # [ql, qr] 在左子树
            return self._query(node * 2, l, m, ql, qr)
        if ql > m:  # [ql, qr] 在右子树
            return self._query(node * 2 + 1, m + 1, r, ql, qr)
        l_res = self._query(node * 2, l, m, ql, qr)
        r_res = self._query(node * 2 + 1, m + 1, r, ql, qr)
        return self._merge_val(l_res, r_res)

    # 更新 a[i] 为 _merge_val(a[i], val)
    # 时间复杂度 O(log n)
    def update(self, i: int, val: int) -> None:
        self._update(1, 0, self._n - 1, i, val)

    # 返回用 _merge_val 合并所有 a[i] 的计算结果，其中 i 在闭区间 [ql, qr] 中
    # 时间复杂度 O(log n)
    def query(self, ql: int, qr: int) -> int:
        return self._query(1, 0, self._n - 1, ql, qr)

    # 获取 a[i] 的值
    # 时间复杂度 O(log n)
    def get(self, i: int) -> int:
        return self._query(1, 0, self._n - 1, i, i)


# 选出所有nums中，是p倍数的数，它们的gcd就是能达到的最小的p的倍数
# 要用线段树，维护各个区间的gcd（仅考虑p的倍数的数，其他数可以忽略）
# 线段树能实现：单点更新，和区间查询
# 另外需要维护nums中，是p倍数的数的个数np
#   1. np<n，那子序列满足题目要求
#   2. 当np超过7时，不需要计算，这个子序列一定存在一个元素，删除之后的gcd一定>p，因此也满足条件（有基本性质决定，这个证明的思维难度很大，是本题最难的地方）
#   3. n==np<7，只需暴力枚举删除一个元素后的子序列是否gcd都为p，即可（在线段树上查询，删除一个元素后的gcd）


class Solution:
    def countGoodSubseq(self, nums: list[int], p: int, queries: list[list[int]]) -> int:
        nums = [x // p if x % p == 0 else 0 for x in nums]
        n = len(nums)
        np = sum(1 for x in nums if x > 0)
        st = SegmentTree(nums)
        ans = 0
        for i, x in queries:
            if nums[i] > 0:
                np -= 1
            if x % p == 0:
                np += 1
            if x % p == 0:
                st.update(i, x // p)
                nums[i] = x // p
            else:
                st.update(i, 0)
                nums[i] = 0
            if st.query(0, n - 1) != 1: continue
            if np < n or np > 6:
                ans += 1
                continue
            # 剩下就是 n==np<7
            if st.query(0, n - 2) == 1 or st.query(1, n - 1) == 1:
                ans += 1
                continue
            for j in range(1, n - 1):
                if gcd(st.query(0, j - 1), st.query(j + 1, n - 1)) == 1:
                    ans += 1
                    break

        return ans



so = Solution()
print(so.countGoodSubseq(nums = [10,15], p = 5, queries = [[0,10]]))
print(so.countGoodSubseq(nums = [15015,10010,6006,4290,2730,2310], p = 1, queries = [[0,15015]]))
print(so.countGoodSubseq(nums = [3,9], p = 9, queries = [[1,3]]))
print(so.countGoodSubseq(nums = [4,8,12,16], p = 2, queries = [[0,3],[2,6]]))




