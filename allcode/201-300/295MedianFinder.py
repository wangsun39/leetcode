# 中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。
#
# 例如 arr = [2,3,4]的中位数是 3。
# 例如arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
# 实现 MedianFinder 类:
#
# MedianFinder() 初始化 MedianFinder对象。
#
# void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
#
# double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差10-5以内的答案将被接受。
#
# 示例 1：
#
# 输入
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# 输出
# [null, null, null, 1.5, null, 2.0]
#
# 解释
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
# 提示:
#
# -105<= num <= 105
# 在调用 findMedian之前，数据结构中至少有一个元素
# 最多5 * 104次调用addNum和findMedian

from leetcode.allcode.competition.mypackage import *

class MedianFinder:

    def __init__(self):
        self.sl = SortedList()


    def addNum(self, num: int) -> None:
        self.sl.add(num)


    def findMedian(self) -> float:
        n = len(self.sl)
        if n & 1:
            return self.sl[n // 2]
        return (self.sl[n // 2] + self.sl[n // 2 - 1]) / 2


so = MedianFinder()




