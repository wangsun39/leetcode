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


class SortedStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        st = []
        while self.stack and self.stack[-1] < val:
            st.append(self.stack.pop())
        self.stack.append(val)
        while st:
            self.stack.append(st.pop())


    def pop(self) -> None:
        if self.isEmpty(): return
        self.stack.pop()

    def peek(self) -> int:
        if self.isEmpty(): return -1
        return self.stack[-1]

    def isEmpty(self) -> bool:
        return len(self.stack) == 0

