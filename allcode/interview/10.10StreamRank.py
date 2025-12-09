# 假设你正在读取一串整数。每隔一段时间，你希望能找出数字 x 的秩(小于或等于 x 的值的个数)。请实现数据结构和算法来支持这些操作，也就是说：
#
# 实现 track(int x) 方法，每读入一个数字都会调用该方法；
#
# 实现 getRankOfNumber(int x) 方法，返回小于或等于 x 的值的个数。
#
# 注意：本题相对原题稍作改动
#
# 示例：
#
# 输入：
# ["StreamRank", "getRankOfNumber", "track", "getRankOfNumber"]
# [[], [1], [0], [0]]
# 输出：
# [null,0,null,1]
# 提示：
#
# x <= 50000
# track 和 getRankOfNumber 方法的调用次数均不超过 2000 次

from leetcode.allcode.competition.mypackage import *

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

class StreamRank:

    def __init__(self):
        self.fw = Fenwick1(50001)

    def track(self, x: int) -> None:
        self.fw.add(x + 1)

    def getRankOfNumber(self, x: int) -> int:
        return self.fw.pre(x + 1)




