# 你有一台电脑，它可以 同时 运行无数个任务。给你一个二维整数数组 tasks ，其中 tasks[i] = [starti, endi, durationi] 表示第 i 个任务需要在 闭区间 时间段 [starti, endi] 内运行 durationi 个整数时间点（但不需要连续）。
#
# 当电脑需要运行任务时，你可以打开电脑，如果空闲时，你可以将电脑关闭。
#
# 请你返回完成所有任务的情况下，电脑最少需要运行多少秒。
#
#
#
# 示例 1：
#
# 输入：tasks = [[2,3,1],[4,5,1],[1,5,2]]
# 输出：2
# 解释：
# - 第一个任务在闭区间 [2, 2] 运行。
# - 第二个任务在闭区间 [5, 5] 运行。
# - 第三个任务在闭区间 [2, 2] 和 [5, 5] 运行。
# 电脑总共运行 2 个整数时间点。
# 示例 2：
#
# 输入：tasks = [[1,3,2],[2,5,3],[5,6,2]]
# 输出：4
# 解释：
# - 第一个任务在闭区间 [2, 3] 运行
# - 第二个任务在闭区间 [2, 3] 和 [5, 5] 运行。
# - 第三个任务在闭区间 [5, 6] 运行。
# 电脑总共运行 4 个整数时间点。
#
#
# 提示：
#
# 1 <= tasks.length <= 2000
# tasks[i].length == 3
# 1 <= starti, endi <= 2000
# 1 <= durationi <= endi - starti + 1

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findMinimumTime1(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1])
        vis = set()
        # print(tasks)
        for l, r, d in tasks:
            cand = []
            for i in range(l, r + 1):
                if i not in vis:
                    cand.append(i)
            need = d - (r - l + 1 - len(cand))
            for i in range(need):
                vis.add(cand[-i - 1])
        # print(vis)
        return len(vis)


    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        # 2024/5/15 扫描线，这个性能不如上面的
        ans = []
        n = len(tasks)
        mn, mx = min(x for x, _, _ in tasks), max(x for _, x, _ in tasks)
        for i in range(mn, mx + 1):
            for t1, t2, d in tasks:
                if d == 0 or i < t1 or i > t2: continue
                if d <= t2 - i: continue
                ans.append(i)
                for j in range(n):
                    if tasks[j][0] <= i <= tasks[j][1]:
                        if tasks[j][2]:
                            tasks[j][2] -= 1
                break
        return len(ans)



so = Solution()
print(so.findMinimumTime([[2,3,1],[4,5,1],[1,5,2]]))   # 4
print(so.findMinimumTime([[1,3,2],[2,5,3],[5,6,2]]))   # 2




