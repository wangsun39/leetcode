# 给定一个数组，包含从 1 到 N 所有的整数，但其中缺了两个数字。你能在 O(N) 时间内只用 O(1) 的空间找到它们吗？
#
# 以任意顺序返回这两个数字均可。
#
# 示例 1:
#
# 输入: [1]
# 输出: [2,3]
# 示例 2:
#
# 输入: [2,3]
# 输出: [1,4]
# 提示：
#
# nums.length <=30000


from leetcode.allcode.competition.mypackage import *


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 对顶堆
        self.dq1 = []
        self.dq2 = []

    def addNum(self, num: int) -> None:
        if len(self.dq1) == 0:
            heappush(self.dq1, -num)
            return
        if num <= -self.dq1[0]:
            heappush(self.dq1, -num)
        else:
            heappush(self.dq2, num)
        if len(self.dq1) > len(self.dq2) + 1:
            x = -heappop(self.dq1)
            heappush(self.dq2, x)
        elif len(self.dq1) < len(self.dq2):
            x = heappop(self.dq2)
            heappush(self.dq1, -x)


    def findMedian(self) -> float:
        if len(self.dq1) == len(self.dq2):
            return (-self.dq1[0] + self.dq2[0]) / 2
        return -self.dq1[0]


so = MedianFinder()
so.addNum(1)
so.addNum(2)
so.addNum(3)
print(so.findMedian())





