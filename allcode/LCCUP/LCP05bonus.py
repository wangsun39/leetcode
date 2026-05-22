# 力扣决定给一个刷题团队发LeetCoin作为奖励。同时，为了监控给大家发了多少LeetCoin，力扣有时候也会进行查询。
#
#
#
# 该刷题团队的管理模式可以用一棵树表示：
#
# 团队只有一个负责人，编号为1。除了该负责人外，每个人有且仅有一个领导（负责人没有领导）；
# 不存在循环管理的情况，如A管理B，B管理C，C管理A。
#
#
# 力扣想进行的操作有以下三种：
#
# 给团队的一个成员（也可以是负责人）发一定数量的LeetCoin；
# 给团队的一个成员（也可以是负责人），以及他/她管理的所有人（即他/她的下属、他/她下属的下属，……），发一定数量的LeetCoin；
# 查询某一个成员（也可以是负责人），以及他/她管理的所有人被发到的LeetCoin之和。
#
#
# 输入：
#
# N表示团队成员的个数（编号为1～N，负责人为1）；
# leadership是大小为(N - 1) * 2的二维数组，其中每个元素[a, b]代表b是a的下属；
# operations是一个长度为Q的二维数组，代表以时间排序的操作，格式如下：
# operations[i][0] = 1: 代表第一种操作，operations[i][1]代表成员的编号，operations[i][2]代表LeetCoin的数量；
# operations[i][0] = 2: 代表第二种操作，operations[i][1]代表成员的编号，operations[i][2]代表LeetCoin的数量；
# operations[i][0] = 3: 代表第三种操作，operations[i][1]代表成员的编号；
# 输出：
#
# 返回一个数组，数组里是每次查询的返回值（发LeetCoin的操作不需要任何返回值）。由于发的LeetCoin很多，请把每次查询的结果模1e9+7 (1000000007)。
#
#
#
# 示例 1：
#
# 输入：N = 6, leadership = [[1, 2], [1, 6], [2, 3], [2, 5], [1, 4]], operations = [[1, 1, 500], [2, 2, 50], [3, 1], [2, 6, 15], [3, 1]]
# 输出：[650, 665]
# 解释：团队的管理关系见下图。
# 第一次查询时，每个成员得到的LeetCoin的数量分别为（按编号顺序）：500, 50, 50, 0, 50, 0;
# 第二次查询时，每个成员得到的LeetCoin的数量分别为（按编号顺序）：500, 50, 50, 0, 50, 15.
#
#
#
#
# 限制：
#
# 1 <= N <= 50000
# 1 <= Q <= 50000
# operations[i][0] != 3 时，1 <= operations[i][2] <= 5000

from leetcode.allcode.competition.mypackage import *

# 模板来源 https://leetcode.cn/circle/discuss/mOr1u6/

MOD = 10 ** 9 + 7

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
        self._tree = [Node() for _ in range(2 << (n - 1).bit_length())]
        self._build(arr, 1, 0, n - 1)

    # 合并两个 val
    def _merge_val(self, a: int, b: int) -> int:
        return (a + b) % MOD  # **根据题目修改**

    # 合并两个懒标记
    def _merge_todo(self, a: int, b: int) -> int:
        return (a + b) % MOD  # **根据题目修改**

    # 把懒标记作用到 node 子树（本例为区间加）
    def _apply(self, node: int, l: int, r: int, todo: int) -> None:
        cur = self._tree[node]
        # 计算 tree[node] 区间的整体变化
        cur.val += todo * (r - l + 1)  # **根据题目修改**
        cur.val %= MOD
        cur.todo = self._merge_todo(todo, cur.todo)

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
    def bonus(self, n: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for a, b in leadership:
            g[a].append(b)

        clock = 0
        in_time = [0] * (n + 1)  # 记录前序遍历时的时间戳
        out_time = [0] * (n + 1)
        # arr[i] 是 按时间戳排在第i位的节点
        arr = []  # 将树转成数组
        mp = [0] * (n + 1)  # 数值映射到arr的下标

        def dfs(x: int, fa: int) -> None:
            nonlocal clock
            mp[x] = len(arr)
            arr.append(x)
            in_time[x] = clock
            clock += 1
            for y in g[x]:
                if y != fa:
                    dfs(y, x)
            out_time[x] = clock
        dfs(1, 0)
        # print(arr)
        # print(in_time)
        # print(out_time)
        # print(mp)
        st = LazySegmentTree([0] * n)
        ans = []
        for op in operations:
            if op[0] == 1:
                # 单点更新
                x, v = op[1], op[2]
                st.update(mp[x], mp[x], v)
            elif op[0] == 2:
                x, v = op[1], op[2]
                L, R = in_time[x], out_time[x]
                st.update(L, R - 1, v)
            else:
                x = op[1]
                L, R = in_time[x], out_time[x]
                ans.append(st.query(L, R - 1))
        return ans



so = Solution()
print(so.bonus(n = 6, leadership = [[1, 2], [1, 6], [2, 3], [2, 5], [1, 4]], operations = [[1, 1, 500], [3, 1], [2, 2, 50], [3, 1], [2, 6, 15], [3, 1]]))




