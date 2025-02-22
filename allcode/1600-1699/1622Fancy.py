# 请你实现三个 API append，addAll 和 multAll 来实现奇妙序列。
#
# 请实现 Fancy 类 ：
#
# Fancy() 初始化一个空序列对象。
# void append(val) 将整数 val 添加在序列末尾。
# void addAll(inc) 将所有序列中的现有数值都增加 inc 。
# void multAll(m) 将序列中的所有现有数值都乘以整数 m 。
# int getIndex(idx) 得到下标为 idx 处的数值（下标从 0 开始），并将结果对 109 + 7 取余。如果下标大于等于序列的长度，请返回 -1 。
#
#
# 示例：
#
# 输入：
# ["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
# [[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
# 输出：
# [null, null, null, null, null, 10, null, null, null, 26, 34, 20]
#
# 解释：
# Fancy fancy = new Fancy();
# fancy.append(2);   // 奇妙序列：[2]
# fancy.addAll(3);   // 奇妙序列：[2+3] -> [5]
# fancy.append(7);   // 奇妙序列：[5, 7]
# fancy.multAll(2);  // 奇妙序列：[5*2, 7*2] -> [10, 14]
# fancy.getIndex(0); // 返回 10
# fancy.addAll(3);   // 奇妙序列：[10+3, 14+3] -> [13, 17]
# fancy.append(10);  // 奇妙序列：[13, 17, 10]
# fancy.multAll(2);  // 奇妙序列：[13*2, 17*2, 10*2] -> [26, 34, 20]
# fancy.getIndex(0); // 返回 26
# fancy.getIndex(1); // 返回 34
# fancy.getIndex(2); // 返回 20
#
#
# 提示：
#
# 1 <= val, inc, m <= 100
# 0 <= idx <= 105
# 总共最多会有 105 次对 append，addAll，multAll 和 getIndex 的调用。

from leetcode.allcode.competition.mypackage import *

MOD = 10 ** 9 + 7

class STree1:
    # Lazy 线段树
    def __init__(self, n):
        self.arr = []
        self.a = [0] * (4 * n)  # 每个区间的 add  默认值为 0
        self.m = [1] * (4 * n)  # 每个区间的 multiply 默认值为 1
        # self.cnt = [0] * (4 * n)  # 记录区间1的个数
        self.todo = [False] * (4 * n)  # 特殊区间的lazy标记

    # (m, a)  (multi, add) => (m * multi, a * multi + add)
    def do(self, o: int, l: int, r: int, multi: int, add: int) -> None:
        self.m[o] *= multi
        self.m[o] %= MOD
        self.a[o] = self.a[o] * multi + add
        self.a[o] %= MOD
        self.todo[o] = True

    def spread(self, o: int, l: int, m: int, r: int, multi: int, add: int) -> None:
        if self.todo[o]:
            self.todo[o] = False
            self.do(o * 2, l, m, multi, add)
            self.do(o * 2 + 1, m + 1, r, multi, add)
            self.m[o] = 1
            self.a[o] = 0

    # 更新区间的倍数
    def update(self, o: int, l: int, r: int, L: int, R: int, multi: int, add: int) -> None:
        # 进入这个函数的前提是，[l,r] 与 [L,R]有交集
        if L <= l and r <= R:
            self.do(o, l, r, multi, add)
            return
        m = (l + r) // 2
        self.spread(o, l, m, r, multi, add)  # 有 lazy tag的区间要被破坏开
        if m >= L: self.update(o * 2, l, m, L, R, multi, add)
        if m < R: self.update(o * 2 + 1, m + 1, r, L, R, multi, add)

    def query(self, o: int, l: int, r: int, idx: int) -> int:
        if l == r:
            return (self.arr[l - 1] * self.m[o] + self.a[o]) % MOD
        m = (l + r) // 2
        self.spread(o, l, m, r, self.m[o], self.a[o])
        if m >= idx: return self.query(o * 2, l, m, idx)
        if m < idx: return self.query(o * 2 + 1, m + 1, r, idx)

class Fancy:

    def __init__(self):
        self.N = 10 ** 5
        self.st = STree1(self.N)

    def append(self, val: int) -> None:
        self.st.arr.append(val)

    def addAll(self, inc: int) -> None:
        if len(self.st.arr) == 0: return
        self.st.update(1, 1, self.N, 1, len(self.st.arr), 1, inc)

    def multAll(self, m: int) -> None:
        if len(self.st.arr) == 0: return
        self.st.update(1, 1, self.N, 1, len(self.st.arr), m, 0)

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.st.arr): return -1
        return self.st.query(1, 1, self.N, idx + 1)



so = Fancy()
print(so.append(2))
print(so.addAll(3))
print(so.append(7))
print(so.multAll(2))
print(so.getIndex(0))
print(so.addAll(3))
print(so.append(10))
print(so.multAll(2))
print(so.getIndex(0))
print(so.getIndex(1))
print(so.getIndex(2))




