# 写一个RecentCounter类来计算特定时间范围内最近的请求。
#
# 请你实现 RecentCounter 类：
#
# RecentCounter() 初始化计数器，请求数为 0 。
# int ping(int t) 在时间 t 添加一个新请求，其中 t 表示以毫秒为单位的某个时间，并返回过去 3000 毫秒内发生的所有请求数（包括新请求）。确切地说，返回在 [t-3000, t] 内发生的请求数。
# 保证 每次对 ping 的调用都使用比之前更大的 t 值。
#
#
#
# 示例 1：
#
# 输入：
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# 输出：
# [null, 1, 2, 3, 3]
#
# 解释：
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1]，范围是 [-2999,1]，返回 1
# recentCounter.ping(100);   // requests = [1, 100]，范围是 [-2900,100]，返回 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001]，范围是 [1,3001]，返回 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002]，范围是 [2,3002]，返回 3
#
#
# 提示：
#
# 1 <= t <= 109
# 保证每次对 ping 调用所使用的 t 值都 严格递增
# 至多调用 ping 方法 104 次


import copy
class RecentCounter:

    def __init__(self):
        self.cur = -1
        self.start = 0
        self.records = []


    def ping(self, t: int) -> int:
        self.cur += 1
        self.records.append(t)
        while self.start < len(self.records) and self.records[self.start] < t - 3000:
            self.start += 1
        return self.cur - self.start + 1


so = RecentCounter()
print(so.ping(1))
print(so.ping(100))
print(so.ping(3001))
print(so.ping(3002))

