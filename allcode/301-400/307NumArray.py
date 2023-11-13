# 给你一个数组 nums ，请你完成两类查询。
#
# 其中一类查询要求 更新 数组 nums 下标对应的值
# 另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right
# 实现 NumArray 类：
#
# NumArray(int[] nums) 用整数数组 nums 初始化对象
# void update(int index, int val) 将 nums[index] 的值 更新 为 val
# int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 （即，nums[left] + nums[left + 1], ..., nums[right]）
#  
#
# 示例 1：
#
# 输入：
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# 输出：
# [null, 9, null, 8]
#
# 解释：
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // 返回 1 + 3 + 5 = 9
# numArray.update(1, 2);   // nums = [1,2,5]
# numArray.sumRange(0, 2); // 返回 1 + 2 + 5 = 8
#  
#
# 提示：
#
# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# 0 <= index < nums.length
# -100 <= val <= 100
# 0 <= left <= right < nums.length
# 调用 update 和 sumRange 方法次数不大于 3 * 104 


from typing import List
from collections import defaultdict
import math


class NumArray1:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.N = len(nums)
        self.partialSum = [0] * self.N
        self.partialSum[0] = self.nums[0]
        for i in range(1, self.N):
            self.partialSum[i] = self.partialSum[i - 1] + nums[i]

        self.minus = [0] * self.N
        self.minus[0] = self.partialSum[0]
        for i in range(1, self.N):
            self.minus[i] = self.partialSum[i] - self.partialSum[i - 1]


    def update(self, index: int, val: int) -> None:
        old = self.nums[index]
        self.nums[index] = val
        self.minus[index] += (val - old)

    def sumRange(self, left: int, right: int) -> int:
        pass

class NumArray1:

    def __init__(self, nums: List[int]):
        self.tree = defaultdict(int)
        n = len(nums)
        self.n = n
        for i in range(n):
            # self.tree[n + i] = nums[i]
            self.update(i, nums[i])
        print(self.tree)


    def update(self, index: int, val: int) -> None:
        # self.update1(1, 0, 3 * (10 ** 4), index, index, val)
        self.update1(1, 0, self.n, index, index, val)


    def sumRange(self, left: int, right: int) -> int:
        # return self.query(1, 0, 3 * (10 ** 4), left, right)
        return self.query(1, 0, self.n, left, right)

    def pushup(self, id: int):
        # if (1 == self.tree[id << 1]) and (1 == self.tree[(id << 1) | 1]):
        #     self.tree[id] = 1
        # else:
        #     self.tree[id] = 0
        self.tree[id] = self.tree[id << 1] + self.tree[(id << 1) | 1]

    def pushdown(self, id: int):
        if self.tree[id]:
            left, right = id << 1, (id << 1) | 1
            self.tree[left] = self.tree[id]
            self.tree[right] = self.tree[id]

    def update1(self, id: int, start: int, end: int, l: int, r: int, val: int):
        if start > r or end < l:
            return
        if start >= l and end <= r:
            self.tree[id] = val
            return
        mid = (start + end) >> 1
        # self.pushdown(id)
        self.update1(id << 1, start, mid, l, r, val)
        self.update1((id << 1) | 1, mid + 1, end, l, r, val)
        self.pushup(id)

    def query(self, id: int, start: int, end: int, l: int, r: int):
        print(start, r)
        if start > r or end < l:
            return 0
        if start >= l and end <= r:
            return self.tree[id]
        mid = (start + end) >> 1
        # self.pushdown(id)
        left = self.query(id << 1, start, mid, l, r)
        right = self.query((id << 1) | 1, mid + 1, end, l, r)
        return left + right

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


class NumArray:
    # 树状数组

    def lowbit(self, i):
        return i & -i

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = [0] * self.n
        self.tree = [0] * (self.n + 1)   # tree[i] 保存右端点为i的关键区间对应值
        for i, x in enumerate(nums):
            self.update(i, x)


    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        i = index + 1
        while i <= self.n:
            self.tree[i] += delta
            i = i + self.lowbit(i)
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.sumPrefix(right + 1) - self.sumPrefix(left)

    def sumPrefix(self, val):
        s = 0
        i = val
        while i:
            s += self.tree[i]
            i = i - self.lowbit(i)
        return s



so = NumArray([1, 3, 5])
print(so.tree)
print(so.sumRange(0, 2))
print(so.update(1, 2))
print(so.sumRange(0, 2))

