# Range模块是跟踪数字范围的模块。设计一个数据结构来跟踪表示为 半开区间 的范围并查询它们。
#
# 半开区间 [left, right) 表示所有 left <= x < right 的实数 x 。
#
# 实现 RangeModule 类:
#
# RangeModule() 初始化数据结构的对象。
# void addRange(int left, int right) 添加 半开区间 [left, right)，跟踪该区间中的每个实数。添加与当前跟踪的数字部分重叠的区间时，应当添加在区间 [left, right) 中尚未跟踪的任何数字到该区间中。
# boolean queryRange(int left, int right) 只有在当前正在跟踪区间 [left, right) 中的每一个实数时，才返回 true ，否则返回 false 。
# void removeRange(int left, int right) 停止跟踪 半开区间 [left, right) 中当前正在跟踪的每个实数。
#  
#
# 示例 1：
#
# 输入
# ["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
# [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
# 输出
# [null, null, null, true, false, true]
#
# 解释
# RangeModule rangeModule = new RangeModule();
# rangeModule.addRange(10, 20);
# rangeModule.removeRange(14, 16);
# rangeModule.queryRange(10, 14); 返回 true （区间 [10, 14) 中的每个数都正在被跟踪）
# rangeModule.queryRange(13, 15); 返回 false（未跟踪区间 [13, 15) 中像 14, 14.03, 14.17 这样的数字）
# rangeModule.queryRange(16, 17); 返回 true （尽管执行了删除操作，区间 [16, 17) 中的数字 16 仍然会被跟踪）
#  
#
# 提示：
#
# 1 <= left < right <= 109
# 在单个测试用例中，对 addRange 、  queryRange 和 removeRange 的调用总数不超过 104 次





from typing import List
from collections import defaultdict


class Node:
    def __init__(self):
        self.val = False
        self.lazy = 0
        self.left = None
        self.right = None

class RangeModule1:
    def __init__(self):
        # self.tree = defaultdict(int)
        self.root = Node()

    def pushup(self, v: Node):
        v.val = v.left.val and v.right.val

    def pushdown(self, v: Node, leftNum, rightNum):
        if v.left is None:
            v.left = Node()
        if v.right is None:
            v.right = Node()
        if v.lazy == 0:
            return
        v.left.val = (v.lazy == 1)
        v.left.lazy = v.lazy
        v.right.val = (v.lazy == 1)
        v.right.lazy = v.lazy
        v.lazy = 0

    def update(self, v: Node, start: int, end: int, l: int, r: int, val: int):
        if start >= l and end <= r:
            v.val = (val == 1)
            v.lazy = val
            return
        mid = (start + end) >> 1
        self.pushdown(v, mid - start + 1, end - mid)
        if mid >= l:
            self.update(v.left, start, mid, l, r, val)
        if mid < r:
            self.update(v.right, mid + 1, end, l, r, v)
        self.pushup(v)

    def query(self, v: Node, start: int, end: int, l: int, r: int):
        if start >= l and end <= r:
            return v.val
        mid = (start + end) >> 1
        self.pushdown(v, mid - start + 1, end - mid)
        if mid >= l:
            if not self.query(v.left, start, mid, l, r):
                return False
        if mid + 1 <= r:
            return self.query(v.right, mid + 1, end, l, r)
        return True


    def addRange(self, left: int, right: int) -> None:
        self.update(self.root, 1, 10 ** 9, left, right - 1, 1)

    def queryRange(self, left: int, right: int) -> bool:
        return self.query(self.root, 1, 10 ** 9, left, right - 1)

    def removeRange(self, left: int, right: int) -> None:
        self.update(self.root, 1, 10 ** 9, left, right - 1, -1)


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


so = RangeModule()
print(so.addRange(10, 20))
print(so.removeRange(14, 16))
print(so.queryRange(10, 14))
print(so.queryRange(13, 15))
print(so.queryRange(16, 17))


