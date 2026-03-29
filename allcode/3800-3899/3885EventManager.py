# 给你一组初始事件列表，其中每个事件有一个唯一的 eventId 和一个 priority（优先级）。
#
# 实现 EventManager 类：
#
# EventManager(int[][] events) 使用给定事件初始化管理器，其中 events[i] = [eventIdi, priorityi]。
# void updatePriority(int eventId, int newPriority) 更新具有 id 为 eventId 的 活跃 事件的优先级为 newPriority。
# int pollHighest() 移除并返回具有 最高优先级 的 活跃事件 的 eventId。如果有多个活动事件具有相同的优先级，则返回 eventId 最小的事件。如果没有活跃事件，则返回 -1。
# 如果一个事件没有被 pollHighest() 移除，则称其为 活跃事件。
#
#
#
# 示例 1：
#
# 输入：
# ["EventManager", "pollHighest", "updatePriority", "pollHighest", "pollHighest"]
# [[[[5, 7], [2, 7], [9, 4]]], [], [9, 7], [], []]
#
# 输出：
# [null, 2, null, 5, 9]
#
# 解释
#
# EventManager eventManager = new EventManager([[5,7], [2,7], [9,4]]); // 使用三个事件初始化管理器
# eventManager.pollHighest(); // 两个事件 5 和 2 的优先级均为 7，因此返回 id 最小的事件 2
# eventManager.updatePriority(9, 7); // 将事件 9 的优先级更新为 7
# eventManager.pollHighest(); // 剩下的优先级最高的事件是 5 和 9，返回 5
# eventManager.pollHighest(); // 返回 9
# 示例 2：
#
# 输入：
# ["EventManager", "pollHighest", "pollHighest", "pollHighest"]
# [[[[4, 1], [7, 2]]], [], [], []]
#
# 输出：
# [null, 7, 4, -1]
#
# 解释
#
# EventManager eventManager = new EventManager([[4,1], [7,2]]); // 使用两个事件初始化管理器
# eventManager.pollHighest(); // 返回 7
# eventManager.pollHighest(); // 返回 4
# eventManager.pollHighest(); // 没有剩余事件，返回 -1
#
#
# 提示：
#
# 1 <= events.length <= 105
# events[i] = [eventId, priority]
# 1 <= eventId <= 109
# 1 <= priority <= 109
# events 中的所有 eventId 值都是 唯一的 。
# 1 <= newPriority <= 109
# 对每次调用 updatePriority，eventId 都指向一个 活跃事件。
# 对 updatePriority 和 pollHighest 的总调用次数最多为 105 次。

from leetcode.allcode.competition.mypackage import *


class EventManager:

    def __init__(self, events: list[list[int]]):
        self.pr = {}
        self.hp = []
        for id, p in events:
            heappush(self.hp, [-p, id])
            self.pr[id] = p

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.pr[eventId] = newPriority
        heappush(self.hp, [-newPriority, eventId])

    def pollHighest(self) -> int:
        while self.hp and (self.hp[0][1] not in self.pr or self.pr[self.hp[0][1]] != -self.hp[0][0]):
            heappop(self.hp)
        if self.hp and self.pr[self.hp[0][1]] == -self.hp[0][0]:
            p, id = heappop(self.hp)
            del(self.pr[id])
            return id
        return -1



so = EventManager([[5, 7], [2, 7], [9, 4]])
print(so.pollHighest())
print(so.updatePriority(9, 7))
print(so.pollHighest())
print(so.pollHighest())




