

from leetcode.allcode.competition.mypackage import *


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_to_pr = {}
        self.hp = []
        for user, task, pr in tasks:
            self.task_to_pr[task] = [pr, user]
            heappush(self.hp, [-pr, -task, user])

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_to_pr[taskId] = [priority, userId]
        heappush(self.hp, [-priority, -taskId, userId])

    def edit(self, taskId: int, newPriority: int) -> None:
        _, userId = self.task_to_pr[taskId]
        self.task_to_pr[taskId] = [newPriority, userId]
        heappush(self.hp, [-newPriority, -taskId, userId])


    def rmv(self, taskId: int) -> None:
        del(self.task_to_pr[taskId])

    def execTop(self) -> int:
        while self.hp:
            pr, task, user = heappop(self.hp)
            pr = -pr
            task = -task
            if task not in self.task_to_pr or self.task_to_pr[task] != [pr, user]:
                continue
            del (self.task_to_pr[task])
            return user
        return -1

so = TaskManager([[1,101,8],[2,102,20],[3,103,5]])
print(so.add(4,104,5))
print(so.edit(102,9))
print(so.execTop())
print(so.rmv(101))
print(so.add(50,101,8))
print(so.execTop())

so = TaskManager([[1,101,8],[2,102,20],[3,103,5]])
print(so.add(4,104,5))
print(so.edit(102,9))
print(so.execTop())
print(so.rmv(101))

so = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])
print(so.add(4, 104, 5))
print(so.edit(102, 8))
print(so.execTop())




