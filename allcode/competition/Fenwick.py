
from leetcode.allcode.competition.mypackage import *

# 数据超过10 ** 5，需要对数据离散化

# 树状数组模板
class Fenwick1:
    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def add(self, i: int) -> None:  # + 1
        while i < len(self.tree):
            self.tree[i] += 1
            i += i & -i

    # [1,i] 中的元素和
    def pre(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.tree[i]
            i &= i - 1
        return res

    # [l,r] 中的元素和
    def query(self, l: int, r: int) -> int:
        return self.pre(r) - self.pre(l - 1)

class Fenwick:
    # 所有函数参数下标从1开始，可以传入使用者的数值x+1的值
    __slots__ = ['f', 'nums']

    def __init__(self, n: int):
        # n 是能调用下面函数的下标最大值
        self.f = [0] * (n + 1)  # 关键区间
        self.nums = [0] * (n + 1)

    def add(self, i: int, val: int) -> None:  # nums[i] += val
        self.nums[i] += val
        while i < len(self.f):
            self.f[i] += val
            i += i & -i

    def update(self, i: int, val: int) -> None:  # nums[i] += val
        delta = val - self.nums[i]
        self.add(i, delta)

    def pre(self, i: int) -> int:  # 下标<=i的和
        res = 0
        while i > 0:
            res += self.f[i]
            i &= i - 1
        return res

    def query_one(self, idx: int):
        return self.nums[idx]

    def query(self, l: int, r: int) -> int:  # [l, r]  区间求和
        if r < l:
            return 0
        return self.pre(r) - self.pre(l - 1)

class Fenwick2:
    # 求前缀最大值（区间求max不能用!!!）
    # 所有函数参数下标从1开始，可以传入使用者的数值x+1的值
    __slots__ = ['f', 'nums']

    def __init__(self, n: int):
        # n 是能调用下面函数的下标最大值
        self.f = [0] * (n + 1)   # 关键区间最大值

    def update(self, i: int, val: int) -> None:  # nums[i] = val
        while i < len(self.f):
            self.f[i] = max(self.f[i], val)
            i += i & -i

    def query(self, i: int) -> int:  # 下标<=i的最大值
        mx = 0
        while i > 0:
            mx = max(mx, self.f[i])
            i &= i - 1
        return mx

