# 给你两个整数数组 tasks 和 shifts。
#
# tasks[i] 表示完成第 ith 个任务所需的时间。
# shifts[j] 表示第 jth 个班次可用的时间。
# 任务 必须 按照从左到右的顺序处理。
#
# 延续处理：如果一个任务在当前班次内没有完成，则下一班次会从该任务的 相同进度位置 继续处理。
# 重新开始：如果一个班次内完成了所有任务，则该班次会 立即结束 。该班次剩余的时间会被 丢弃，下一班次会重新从第 0 个任务开始。
# 如果一个任务尚未被完全完成，则认为该任务是 未完成 的。这包括当前正在执行中的任务。
#
# 返回一个整数数组 ans，其中 ans[j] 表示第 jth 个班次结束后剩余的 未完成 任务数量。
#
#
#
# 示例 1：
#
# 输入： tasks = [1,4,4], shifts = [9,1,4]
#
# 输出： [0,2,1]
#
# 解释：
#
# 班次 0：所有任务需要 1 + 4 + 4 = 9 单位时间，因此全部完成。未完成任务数量为 0。
# 班次 1：重新从任务 0 开始处理。该班次有 1 单位时间，因此任务 0 完成。未完成任务数量为 2。
# 班次 2：从任务 1 的当前位置继续处理。该班次有 4 单位时间，因此任务 1 完成。未完成任务数量为 1。
# 示例 2：
#
# 输入： tasks = [2,3,4], shifts = [20,4,5]
#
# 输出： [0,2,0]
#
# 解释：
#
# 班次 0：所有任务需要 2 + 3 + 4 = 9 单位时间，因此全部完成。剩余时间被忽略。未完成任务数量为 0。
# 班次 1：重新从任务 0 开始处理。该班次有 4 单位时间，因此任务 0 完成，任务 1 只完成了一部分。未完成任务数量为 2。
# 班次 2：从任务 1 的当前位置继续处理。剩余所需时间为 1 + 4 = 5，因此所有任务完成。未完成任务数量为 0。
# 示例 3：
#
# 输入： tasks = [4,2], shifts = [3,6,1]
#
# 输出： [2,0,2]
#
# 解释：
#
# 班次 0：该班次有 3 单位时间，因此任务 0 被部分完成，剩余 1 单位工作量。未完成任务数量为 2。
# 班次 1：继续处理任务 0。剩余所需时间为 1 + 2 = 3，因此所有任务完成。未完成任务数量为 0。
# 班次 2：重新从任务 0 开始处理。该班次有 1 单位时间，因此任务 0 被部分完成。未完成任务数量为 2。
#
#
# 提示：
#
# 1 <= tasks.length <= 105
# 1 <= shifts.length <= 105
# 1 <= tasks[i] <= 109
# 1 <= shifts[i] <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        s = list(accumulate(tasks, initial=0))
        n = len(tasks)
        ans = [0] * len(shifts)
        cp = cv = 0
        for i, x in enumerate(shifts):
            if s[n] - s[cp] - cv <= x:
                cp = cv = 0
                ans[i] = 0
            else:
                if tasks[cp] - cv > x:
                    cv += x
                    ans[i] = n - cp
                    continue
                x -= (tasks[cp] - cv)
                cp += 1
                cv = 0
                if x == 0:
                    ans[i] = n - cp
                    continue
                # 找到一个第一个位置j，使得 s[j+1]-s[cp]>=x，即 s[j+1]>=x+s[cp]
                p = bisect_left(s, x + s[cp])
                if s[p] == x + s[cp] + cv:
                    ans[i] = n - p
                    cp = p % n
                    cv = 0
                else:
                    ans[i] = n - (p - 1)
                    cp = p - 1
                    cv = tasks[p] - (s[p] - s[cp] - cv - x)

        return ans


so = Solution()
print(so.countTasks(tasks = [1,4,4], shifts = [9,1,4]))



