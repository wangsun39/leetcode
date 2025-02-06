# 设计一个数据结构，有效地找到给定子数组的 多数元素 。
#
# 子数组的 多数元素 是在子数组中出现 threshold 次数或次数以上的元素。
#
# 实现 MajorityChecker 类:
#
# MajorityChecker(int[] arr) 会用给定的数组 arr 对 MajorityChecker 初始化。
# int query(int left, int right, int threshold) 返回子数组中的元素  arr[left...right] 至少出现 threshold 次数，如果不存在这样的元素则返回 -1。
#
#
# 示例 1：
#
# 输入:
# ["MajorityChecker", "query", "query", "query"]
# [[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
# 输出：
# [null, 1, -1, 2]
#
# 解释：
# MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
# majorityChecker.query(0,5,4); // 返回 1
# majorityChecker.query(0,3,3); // 返回 -1
# majorityChecker.query(2,3,2); // 返回 2
#
#
# 提示：
#
# 1 <= arr.length <= 2 * 104
# 1 <= arr[i] <= 2 * 104
# 0 <= left <= right < arr.length
# threshold <= right - left + 1
# 2 * threshold > right - left + 1
# 调用 query 的次数最多为 104

from random import randint
from leetcode.allcode.competition.mypackage import *


class MajorityChecker1:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.stat = defaultdict(list)
        for i, x in enumerate(arr):
            self.stat[x].append(i)


    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(20): # 进行 20 次随机选择
            r = self.arr[randint(left, right)]  # 计算随机数在区间内出现的次数
            n = right - left + 1
            mi = bisect_left(self.stat[r], left)
            mx = bisect_right(self.stat[r], right)
            t = mx - mi
            if t >= threshold:
                return r
            elif t * 2 >= n:
                return -1
        return -1

# 以下是线段树的方法，线段树记录每个区间，出现次数最多的元素，及其出现次数
# 出现次数是和其他元素比较之后剩余的次数，类似一种打擂台的结果，这种方式仅适用于找到绝对众数
# 参考 https://leetcode.cn/problems/online-majority-element-in-subarray/solutions/19976/san-chong-fang-fa-bao-li-fen-kuai-xian-duan-shu-by
class STree2:
    # 非动态开点，单点更新，区间查询
    def __init__(self, n: int):
        self.element = [0] * (2 << n.bit_length())  # 出现次数最多的元素，0表示不存在
        self.count = [0] * (2 << n.bit_length())  # 出现次数最多的元素出现的次数

    # 线段树：把下标 i 上的元素值增加 val，单点更新
    # o 是当前区间对应的下标，[l, r]当前区间的范围
    def update(self, o: int, l: int, r: int, i: int, val: int) -> None:
        if l == r:
            self.element[o] = val
            self.count[o] = 1
            return
        m = (l + r) // 2
        if i <= m:
            self.update(o * 2, l, m, i, val)
        else:
            self.update(o * 2 + 1, m + 1, r, i, val)
        if self.element[o * 2] == self.element[o * 2 + 1]:
            self.element[o] = self.element[o * 2]
            self.count[o] = self.count[o * 2] + self.count[o * 2 + 1]
        elif self.count[o * 2] >= self.count[o * 2 + 1]:
            self.element[o] = self.element[o * 2]
            self.count[o] = self.count[o * 2] - self.count[o * 2 + 1]
        else:
            self.element[o] = self.element[o * 2 + 1]
            self.count[o] = self.count[o * 2 + 1] - self.count[o * 2]

    # 线段树：返回区间 [L,R] 内的众数，及其出现次数，如果区间内存在绝对众数，这里一定会返回绝对众数
    # 如果不存在绝对众数，这里返回的不一定是众数，这点很重要，次方法不适合查询普通众数
    def query(self, o: int, l: int, r: int, L: int, R: int) -> [int, int]:
        if L <= l and r <= R:
            return [self.element[o], self.count[o]]
        m = (l + r) // 2
        if L > m:
            return self.query(o * 2 + 1, m + 1, r, L, R)
        if R <= m:
            return self.query(o * 2, l, m, L, R)

        v1, c1 = self.query(o * 2, l, m, L, R)
        v2, c2 = self.query(o * 2 + 1, m + 1, r, L, R)

        if v1 == v2:
            return [v1, c1 + c2]
        elif c1 >= c2:
            return [v1, c1 - c2]
        else:
            return [v2, c2 - c1]


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.st = STree2(len(arr))
        self.dd = defaultdict(list)
        for i, x in enumerate(arr):
            self.st.update(1, 1, self.n, i + 1, x)
            self.dd[x].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        val, _ = self.st.query(1, 1, self.n, left + 1, right + 1)  # 找一个出现次数最多的数，但不一定是绝对众数，下面要验证是否是绝对众数
        num = bisect_right(self.dd[val], right) - bisect_left(self.dd[val], left)
        if num >= threshold:
            return val
        return -1


# ["MajorityChecker","query","query","query","query","query","query","query","query","query","query"]
# [[[2,2,1,2,1,2,2,1,1,2]],[2,5,4],[0,5,6],[0,1,2],[2,3,2],[6,6,1],[0,3,3],[4,9,6],[4,8,4],[5,9,5],[0,1,2]]

# Your MajorityChecker object will be instantiated and called as such:
obj = MajorityChecker([2,1,1,1,2,1,2,1,2,2,1,1,2])
print(obj.query(0,6,4))
obj = MajorityChecker([2,2,1,2,1,2,2,1,1,2])
print(obj.query(0,1,2))

obj = MajorityChecker([1, 1, 2, 2, 1, 1])
print(obj.query(0, 5, 4))
print(obj.query(0, 3, 3))
print(obj.query(2, 3, 2))


