# 给你一个长度为 n 的整数数组 nums，以及一个二维整数数组 queries，其中 queries[i] = [idx, val]。
#
# 对于每个查询：
#
# 更新 nums[idx] = val。
# 选择一个满足 1 <= k < n 的整数 k ，将数组分为非空前缀 nums[0..k-1] 和后缀 nums[k..n-1]，使得每部分中 不同 质数的数量之和 最大 。
# 注意：每次查询对数组的更改将持续到后续的查询中。
#
# 返回一个数组，包含每个查询的结果，按给定的顺序排列。
#
# 质数是大于 1 的自然数，只有 1 和它本身两个因数。
#
#
#
# 示例 1：
#
# 输入: nums = [2,1,3,1,2], queries = [[1,2],[3,3]]
#
# 输出: [3,4]
#
# 解释:
#
# 初始时 nums = [2, 1, 3, 1, 2]。
# 在第一次查询后，nums = [2, 2, 3, 1, 2]。将 nums 分为 [2] 和 [2, 3, 1, 2]。[2] 包含 1 个不同的质数，[2, 3, 1, 2] 包含 2 个不同的质数。所以此查询的答案是 1 + 2 = 3。
# 在第二次查询后，nums = [2, 2, 3, 3, 2]。将 nums 分为 [2, 2, 3] 和 [3, 2]，其答案为 2 + 2 = 4。
# 最终输出为 [3, 4]。
# 示例 2：
#
# 输入: nums = [2,1,4], queries = [[0,1]]
#
# 输出: [0]
#
# 解释:
#
# 初始时 nums = [2, 1, 4]。
# 在第一次查询后，nums = [1, 1, 4]。此时数组中没有质数，因此此查询的答案为 0。
# 最终输出为 [0]。
#
#
# 提示：
#
# 2 <= n == nums.length <= 5 * 104
# 1 <= queries.length <= 5 * 104
# 1 <= nums[i] <= 105
# 0 <= queries[i][0] < nums.length
# 1 <= queries[i][1] <= 105

from leetcode.allcode.competition.mypackage import *

MAX = lambda a, b: b if b > a else a

def euler_all_primes(n):
    is_prime = [False, False] + [True] * (n - 1)
    primes = []
    flg = False
    for i in range(2, n + 1):
        if is_prime[i]: primes.append(i)
        if flg: continue
        for j in primes:
            if j * i > n: break
            is_prime[j * i] = False
            if i % j == 0: break

    return is_prime

primes = euler_all_primes(10 ** 5 + 1)

class Node:
    __slots__ = 'val', 'todo'

class LazySegmentTree:
    # 懒标记初始值
    _TODO_INIT = 0  # **根据题目修改**

    def __init__(self, arr, default=0):
        # 线段树维护一个长为 n 的数组（下标从 0 到 n-1）
        # arr 可以是 list 或者 int
        # 如果 arr 是 int，视作数组大小，默认值为 default
        if isinstance(arr, int):
            arr = [default] * arr
        n = len(arr)
        self._n = n
        self._tree = [Node() for _ in range(2 << (n - 1).bit_length())]  # 此线段树维护区间上的最大值
        self._build(arr, 1, 0, n - 1)

    # 合并两个 val
    def _merge_val(self, a: int, b: int) -> int:
        return MAX(a, b)  # **根据题目修改**

    # 合并两个懒标记
    def _merge_todo(self, a: int, b: int) -> int:
        return a + b  # **根据题目修改**

    # 把懒标记作用到 node 子树（本例为区间加）
    def _apply(self, node: int, l: int, r: int, todo: int) -> None:
        cur = self._tree[node]
        # 计算 tree[node] 区间的整体变化
        cur.val += todo  # **根据题目修改**  val 维护区间最大值
        cur.todo += todo  # 表示子树每个点要加 todo 的值

    # 把当前节点的懒标记下传给左右儿子
    def _spread(self, node: int, l: int, r: int) -> None:
        todo = self._tree[node].todo
        if todo == self._TODO_INIT:  # 没有需要下传的信息
            return
        m = (l + r) // 2
        self._apply(node * 2, l, m, todo)
        self._apply(node * 2 + 1, m + 1, r, todo)
        self._tree[node].todo = self._TODO_INIT  # 下传完毕

    # 合并左右儿子的 val 到当前节点的 val
    def _maintain(self, node: int) -> None:
        self._tree[node].val = self._merge_val(self._tree[node * 2].val, self._tree[node * 2 + 1].val)

    # 用 a 初始化线段树
    # 时间复杂度 O(n)
    def _build(self, a: List[int], node: int, l: int, r: int) -> None:
        self._tree[node].todo = self._TODO_INIT
        if l == r:  # 叶子
            self._tree[node].val = a[l]  # 初始化叶节点的值
            return
        m = (l + r) // 2
        self._build(a, node * 2, l, m)  # 初始化左子树
        self._build(a, node * 2 + 1, m + 1, r)  # 初始化右子树
        self._maintain(node)

    def _update(self, node: int, l: int, r: int, ql: int, qr: int, f: int) -> None:
        if ql <= l and r <= qr:  # 当前子树完全在 [ql, qr] 内
            self._apply(node, l, r, f)
            return
        self._spread(node, l, r)
        m = (l + r) // 2
        if ql <= m:  # 更新左子树
            self._update(node * 2, l, m, ql, qr, f)
        if qr > m:  # 更新右子树
            self._update(node * 2 + 1, m + 1, r, ql, qr, f)
        self._maintain(node)

    def _query(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql <= l and r <= qr:  # 当前子树完全在 [ql, qr] 内
            return self._tree[node].val
        self._spread(node, l, r)
        m = (l + r) // 2
        if qr <= m:  # [ql, qr] 在左子树
            return self._query(node * 2, l, m, ql, qr)
        if ql > m:  # [ql, qr] 在右子树
            return self._query(node * 2 + 1, m + 1, r, ql, qr)
        l_res = self._query(node * 2, l, m, ql, qr)
        r_res = self._query(node * 2 + 1, m + 1, r, ql, qr)
        return self._merge_val(l_res, r_res)

    # 用 f 更新 [ql, qr] 中的每个 a[i]
    # 0 <= ql <= qr <= n-1
    # 时间复杂度 O(log n)
    def update(self, ql: int, qr: int, f: int) -> None:
        self._update(1, 0, self._n - 1, ql, qr, f)

    # 返回用 _merge_val 合并所有 a[i] 的计算结果，其中 i 在闭区间 [ql, qr] 中
    # 0 <= ql <= qr <= n-1
    # 时间复杂度 O(log n)
    def query(self, ql: int, qr: int) -> int:
        return self._query(1, 0, self._n - 1, ql, qr)


class Solution:
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        pos = defaultdict(SortedList)  # 记录每个质数的下标
        n = len(nums)
        counter = Counter()
        np = 0  # 记录全局不同的质数个数
        for i, x in enumerate(nums):
            if not primes[x]: continue
            pos[x].add(i)
            counter[x] += 1
            if counter[x] == 1:
                np += 1
        st = LazySegmentTree([0] * (n - 1))  # n - 1的分割点, 线段树维护每个分割点能增加的贡献值（除了np之外）
        for k, arr in pos.items():
            if len(arr) <= 1: continue
            l = arr[0]
            r = arr[-1] - 1
            st.update(l, r, 1)  # 分割点在l, r之间时，答案会在np基础上+1

        ans = []
        for i, x in queries:
            y = nums[i]
            if primes[y]:
                counter[y] -= 1
                if counter[y] == 0:
                    np -= 1
                if len(pos[y]) > 1:
                    if i == pos[y][0]:
                        st.update(i, pos[y][1] - 1, -1)  #
                    elif i == pos[y][-1]:
                        st.update(pos[y][-2], i - 1, -1)  #
                pos[y].remove(i)

            if primes[x]:
                if len(pos[x]):
                    if i < pos[x][0]:
                        st.update(i, pos[x][0] - 1, 1)
                    elif i > pos[x][-1]:
                        st.update(pos[x][-1], i - 1, 1)
                pos[x].add(i)
                counter[x] += 1
                if counter[x] == 1:
                    np += 1
            nums[i] = x
            ans.append(np + st.query(0, n - 1))

        return ans





so = Solution()
print(so.maximumCount(nums = [2,1,3,1,2], queries = [[1,2],[3,3]]))




