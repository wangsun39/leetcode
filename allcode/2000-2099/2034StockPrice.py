# 给你一支股票价格的数据流。数据流中每一条记录包含一个 时间戳和该时间点股票对应的 价格。
#
# 不巧的是，由于股票市场内在的波动性，股票价格记录可能不是按时间顺序到来的。某些情况下，有的记录可能是错的。如果两个有相同时间戳的记录出现在数据流中，前一条记录视为错误记录，后出现的记录 更正前一条错误的记录。
#
# 请你设计一个算法，实现：
#
# 更新 股票在某一时间戳的股票价格，如果有之前同一时间戳的价格，这一操作将更正之前的错误价格。
# 找到当前记录里 最新股票价格。最新股票价格定义为时间戳最晚的股票价格。
# 找到当前记录里股票的 最高价格。
# 找到当前记录里股票的 最低价格。
# 请你实现StockPrice类：
#
# StockPrice()初始化对象，当前无股票价格记录。
# void update(int timestamp, int price)在时间点 timestamp更新股票价格为 price。
# int current()返回股票 最新价格。
# int maximum()返回股票 最高价格。
# int minimum()返回股票 最低价格。
#
#
# 示例 1：
#
# 输入：
# ["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
# [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
# 输出：
# [null, null, null, 5, 10, null, 5, null, 2]
#
# 解释：
# StockPrice stockPrice = new StockPrice();
# stockPrice.update(1, 10); // 时间戳为 [1] ，对应的股票价格为 [10] 。
# stockPrice.update(2, 5);  // 时间戳为 [1,2] ，对应的股票价格为 [10,5] 。
# stockPrice.current();     // 返回 5 ，最新时间戳为 2 ，对应价格为 5 。
# stockPrice.maximum();     // 返回 10 ，最高价格的时间戳为 1 ，价格为 10 。
# stockPrice.update(1, 3);  // 之前时间戳为 1 的价格错误，价格更新为 3 。
#                           // 时间戳为 [1,2] ，对应股票价格为 [3,5] 。
# stockPrice.maximum();     // 返回 5 ，更正后最高价格为 5 。
# stockPrice.update(4, 2);  // 时间戳为 [1,2,4] ，对应价格为 [3,5,2] 。
# stockPrice.minimum();     // 返回 2 ，最低价格时间戳为 4 ，价格为 2 。
#
#
# 提示：
#
# 1 <= timestamp, price <= 109
# update，current，maximum和minimum总 调用次数不超过105。
# current，maximum和minimum被调用时，update操作 至少已经被调用过 一次。




from leetcode.allcode.competition.mypackage import *
# Definition for a binary tree node.
class StockPrice1:

    def __init__(self):
        self.d = {}
        self.prices = []
        self.newest = 0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.d:
            pos = bisect.bisect_left(self.prices, self.d[timestamp])
            del(self.prices[pos])
        bisect.insort(self.prices, price)
        self.d[timestamp] = price
        self.newest = max(timestamp, self.newest)

    def current(self) -> int:
        return self.d[self.newest]

    def maximum(self) -> int:
        return self.prices[-1]

    def minimum(self) -> int:
        return self.prices[0]


from sortedcontainers import SortedList, SortedDict

class StockPrice:
    # 2023/10/8 using SortedList
    def __init__(self):
        self.d = {}
        self.sl = SortedList()
        self.curDate = 0


    def update(self, timestamp: int, price: int) -> None:
        if self.curDate < timestamp:
            self.curDate = timestamp
        if timestamp in self.d:
            self.sl.remove(self.d[timestamp])
        self.d[timestamp] = price
        self.sl.add(price)


    def current(self) -> int:
        return self.d[self.curDate]


    def maximum(self) -> int:
        return self.sl[-1]


    def minimum(self) -> int:
        return self.sl[0]


