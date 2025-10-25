
from leetcode.allcode.competition.mypackage import *

class RangeModule:


    def __init__(self):
        self.tree = defaultdict(int)

    def pushup(self, id: int):
        if (1 == self.tree[id << 1]) and (1 == self.tree[(id << 1) | 1]):
            self.tree[id] = 1
        else:
            self.tree[id] = 0

    def pushdown(self, id: int):
        if self.tree[id]:
            left, right = id << 1, (id << 1) | 1
            self.tree[left] = self.tree[id]
            self.tree[right] = self.tree[id]

    def update(self, id: int, start: int, end: int, l: int, r: int, val: int):
        if start > r or end < l:
            return
        if start >= l and end <= r:
            self.tree[id] = val
            return
        mid = (start + end) >> 1
        self.pushdown(id)
        self.update(id << 1, start, mid, l, r, val)
        self.update((id << 1) | 1, mid + 1, end, l, r, val)
        self.pushup(id)

    def query(self, id: int, start: int, end: int, l: int, r: int):
        if start > r or end < l:
            return True
        if start >= l and end <= r:
            return self.tree[id] == 1
        mid = (start + end) >> 1
        self.pushdown(id)
        left = self.query(id << 1, start, mid, l, r)
        if not left:
            return False
        return self.query((id << 1) | 1, mid + 1, end, l, r)


    def addRange(self, left: int, right: int) -> None:
        self.update(1, 1, 10 ** 9, left, right - 1, 1)

    def queryRange(self, left: int, right: int) -> bool:
        return self.query(1, 1, 10 ** 9, left, right - 1)

    def removeRange(self, left: int, right: int) -> None:
        self.update(1, 1, 10 ** 9, left, right - 1, 2)


# 2569
class Solution2:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        todo = [False] * (4 * n)  # 特殊区间的lazy标记

        # # 维护区间 1 的个数
        # def maintain(o: int) -> None:
        #     cnt1[o] = cnt1[o * 2] + cnt1[o * 2 + 1]
        #
        # # 执行区间反转
        # def do(o: int, l: int, r: int) -> None:
        #     cnt1[o] = r - l + 1 - cnt1[o]
        #     todo[o] = not todo[o]

        # 初始化线段树   o,l,r=1,1,n
        def build(o: int, l: int, r: int) -> None:
            if l == r:
                # ...
                return
            m = (l + r) // 2
            build(o * 2, l, m)
            build(o * 2 + 1, m + 1, r)
            # ... maintain(o)

        # 反转区间 [L,R]   o,l,r=1,1,n
        def update(o: int, l: int, r: int, L: int, R: int) -> None:
            # 进入这个函数的前提是，[l,r] 与 [L,R]有交集
            if L <= l and r <= R:
                # ... do(o, l, r)
                return
            m = (l + r) // 2
            # if todo[o]:  # 有 lazy tag的区间要被破坏开
            #     do(o * 2, l, m)
            #     do(o * 2 + 1, m + 1, r)
            #     todo[o] = False
            if m >= L: update(o * 2, l, m, L, R)
            if m < R: update(o * 2 + 1, m + 1, r, L, R)
            # ... maintain(o)

        # build(1, 1, n)
        # ans, s = [], sum(nums2)
        # for op, l, r in queries:  # 注意定义的l 和 r 是从0还是1开始
        #     if op == 1: update(1, 1, n, l + 1, r + 1)
        #     elif op == 2: s += l * cnt1[1]
        #     else: ans.append(s)
        # return ans


# 只能应对 n <= 10 ** 5 的范围
class BookMyShow:
    def __init__(self, n: int):
        self.n = n
        self.min = [0] * (2 << n.bit_length())  # 相比 4n 空间更小
        self.sum = [0] * (2 << n.bit_length())

    # 线段树：把下标 i 上的元素值增加 val，单点更新
    # o 是当前区间对应的下标，[l, r]当前区间的范围
    def update(self, o: int, l: int, r: int, i: int, val: int) -> None:
        if l == r:
            self.min[o] += val
            self.sum[o] += val
            return
        m = (l + r) // 2
        if i <= m:
            self.update(o * 2, l, m, i, val)
        else:
            self.update(o * 2 + 1, m + 1, r, i, val)
        self.min[o] = min(self.min[o * 2], self.min[o * 2 + 1])
        self.sum[o] = self.sum[o * 2] + self.sum[o * 2 + 1]

    # 线段树：返回区间 [L,R] 内的元素和，区间查询和
    def query_sum(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if L <= l and r <= R:
            return self.sum[o]
        res = 0
        m = (l + r) // 2
        if L <= m:
            res = self.query_sum(o * 2, l, m, L, R)
        if R > m:
            res += self.query_sum(o * 2 + 1, m + 1, r, L, R)
        return res

    # 线段树：返回区间 [L,R] 内的元素和，区间查询最小值
    def query_min(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if L <= l and r <= R:
            return self.min[o]
        res = inf
        m = (l + r) // 2
        if L <= m:
            res = min(res, self.query_min(o * 2, l, m, L, R))
        if R > m:
            res = min(res, self.query_min(o * 2 + 1, m + 1, r, L, R))
        return res


class STree1:
    # Lazy 线段树
    def __init__(self, nums: List[int]):
        self.nums = nums
        n = len(nums)
        self.cnt = [0] * (4 * n)  # 记录区间1的个数
        self.todo = [False] * (4 * n)  # 特殊区间的lazy标记

    # 维护区间 1 的个数
    def maintain(self, o: int) -> None:
        self.cnt[o] = self.cnt[o * 2] + self.cnt[o * 2 + 1]

    # 执行区间反转
    def do(self, o: int, l: int, r: int) -> None:
        self.cnt[o] = r - l + 1 - self.cnt[o]
        self.todo[o] = not self.todo[o]

    # 初始化线段树   o,l,r=1,1,n
    def build(self, o: int, l: int, r: int) -> None:
        if l == r:
            self.cnt[o] = self.nums[l - 1]
            return
        m = (l + r) // 2
        self.build(o * 2, l, m)
        self.build(o * 2 + 1, m + 1, r)
        self.maintain(o)

    def spread(self, o: int, l: int, m: int, r: int) -> None:
        if self.todo[o]:
            self.todo[o] = False
            self.do(o * 2, l, m)
            self.do(o * 2 + 1, m + 1, r)

    # 反转区间 [L,R]   o,l,r=1,1,n
    def update(self, o: int, l: int, r: int, L: int, R: int) -> None:
        # 进入这个函数的前提是，[l,r] 与 [L,R]有交集
        if L <= l and r <= R:
            self.do(o, l, r)
            return
        m = (l + r) // 2
        self.spread(o, l, m, r)  # 有 lazy tag的区间要被破坏开
        if m >= L: self.update(o * 2, l, m, L, R)
        if m < R: self.update(o * 2 + 1, m + 1, r, L, R)
        self.maintain(o)

    def query(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if L <= l and r <= R: return self.cnt[o]
        m = (l + r) // 2
        self.spread(o, l, m, r)
        if m >= L: self.query(o * 2, l, m, L, R)
        if m < R: self.query(o * 2 + 1, m + 1, r, L, R)
        self.maintain(o)
        return self.cnt[o]


    # build(1, 1, n)
    # ans, s = [], sum(nums2)
    # for op, l, r in queries:  # 注意定义的l 和 r 是从0还是1开始
    #     if op == 1: update(1, 1, n, l + 1, r + 1)
    #     elif op == 2: s += l * self.cnt[1]
    #     else: ans.append(s)
    # return ans

class STree2:
    # 非动态开点，单点更新，区间查询
    def __init__(self, n: int):
        # self.n = n
        self.max = [0] * (2 << n.bit_length())  # 相比 4n 空间更小

    # 线段树：把下标 i 上的元素值增加 val，单点更新
    # o 是当前区间对应的下标，[l, r]当前区间的范围
    # 调用入口update(1,1,n,...) 或 update(1,0,n-1,...) 根据实际需要填写，l和r一般和L和R的范围一致就可以，不会产生越界
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

# 模板来源 https://leetcode.cn/circle/discuss/mOr1u6/
# 线段树有两个下标，一个是线段树节点的下标，另一个是线段树维护的区间的下标
# 节点的下标：从 1 开始，如果你想改成从 0 开始，需要把左右儿子下标分别改成 node*2+1 和 node*2+2
# 区间的下标：从 0 开始
# 普通线段树
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
        return max(a, b)  # **根据题目修改**

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
            self._tree[node] = self._merge_val(self._tree[node], val)
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



