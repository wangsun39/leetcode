# 栈排序。 编写程序，对栈进行排序使最小元素位于栈顶。最多只能使用一个其他的临时栈存放数据，但不得将元素复制到别的数据结构（如数组）中。该栈支持如下操作：push、pop、peek 和 isEmpty。当栈为空时，peek 返回 -1。
#
# 示例 1：
#
#  输入：
# ["SortedStack", "push", "push", "peek", "pop", "peek"]
# [[], [1], [2], [], [], []]
#  输出：
# [null,null,null,1,null,2]
# 示例 2：
#
#  输入：
# ["SortedStack", "pop", "pop", "push", "pop", "isEmpty"]
# [[], [], [], [1], [], []]
#  输出：
# [null,null,null,null,null,true]
# 提示：
#
# 栈中的元素数目在[0, 5000]范围内。

from leetcode.allcode.competition.mypackage import *


class TripleInOne:

    def __init__(self, stackSize: int):
        self.nums = [0] * stackSize * 3
        self.p=[0, stackSize, stackSize * 2]
        self.n = stackSize

    def push(self, stackNum: int, value: int) -> None:
        if self.p[stackNum] < self.n * (stackNum + 1):
            self.nums[self.p[stackNum]] = value
            self.p[stackNum] += 1

    def pop(self, stackNum: int) -> int:
        if self.isEmpty(stackNum):
            return -1
        self.p[stackNum] -= 1
        return self.nums[self.p[stackNum]]

    def peek(self, stackNum: int) -> int:
        if self.isEmpty(stackNum):
            return -1
        return self.nums[self.p[stackNum] - 1]

    def isEmpty(self, stackNum: int) -> bool:
        return self.p[stackNum] == stackNum * self.n

