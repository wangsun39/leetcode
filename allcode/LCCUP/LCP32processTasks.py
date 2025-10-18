# 某实验室计算机待处理任务以 [start,end,period] 格式记于二维数组 tasks，表示完成该任务的时间范围为起始时间 start 至结束时间 end 之间，需要计算机投入 period 的时长，注意：
#
# period 可为不连续时间
# 首尾时间均包含在内
# 处于开机状态的计算机可同时处理任意多个任务，请返回电脑最少开机多久，可处理完所有任务。
#
# 示例 1：
#
# 输入：tasks = [[1,3,2],[2,5,3],[5,6,2]]
#
# 输出：4
#
# 解释： tasks[0] 选择时间点 2、3； tasks[1] 选择时间点 2、3、5； tasks[2] 选择时间点 5、6； 因此计算机仅需在时间点 2、3、5、6 四个时刻保持开机即可完成任务。
#
# 示例 2：
#
# 输入：tasks = [[2,3,1],[5,5,1],[5,6,2]]
#
# 输出：3
#
# 解释： tasks[0] 选择时间点 2 或 3； tasks[1] 选择时间点 5； tasks[2] 选择时间点 5、6； 因此计算机仅需在时间点 2、5、6 或 3、5、6 三个时刻保持开机即可完成任务。
#
# 提示：
#
# 2 <= tasks.length <= 10^5
# tasks[i].length == 3
# 0 <= tasks[i][0] <= tasks[i][1] <= 10^9
# 1 <= tasks[i][2] <= tasks[i][1]-tasks[i][0] + 1

from leetcode.allcode.competition.mypackage import *

class Solution:
    def processTasks(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1])
        stack = [[tasks[0][1] - tasks[0][2] + 1, tasks[0][1], tasks[0][2]]]  # 存放连续被选择的区间，最后一个值的stack的前缀和
        for l, r, d in tasks[1:]:
            p = bisect_left(stack, [l])
            # 需要计算[l, r] 与 stack[p - 1:] 中所有区间的交集中点数量
            # 其中stack[p:] 的所有区间是被[l,r]完整覆盖的
            # stack[p - 1] 后半有 [l,r] 可能有交集
            if p:
                l0, r0, d0 = stack[p - 1]
                # stack[p:] 的所有区间
                d -= stack[-1][2] - d0
                # stack[p - 1] 后半有 [l,r] 可能有交集
                d -= max(r0 - l + 1, 0)
            else:
                d -= stack[-1][2]
            # 还需要在stack中，再添加d个点，从 r向左找空位
            if d <= 0: continue
            cur = r
            while stack and cur - stack[-1][1] <= d:
                d -= cur - stack[-1][1]
                cur = stack[-1][0]
                stack.pop()
            if cur == r:
                stack.append([r - d + 1, r, stack[-1][2] + d])
            elif stack:
                stack.append([cur - d, r, r - (cur - d) + 1 + stack[-1][2]])
            else:
                stack.append([cur - d, r, r - (cur - d) + 1])
        return stack[-1][2]



so = Solution()
print(so.processTasks([[1,3,2],[2,5,3],[5,6,2]]))  # 4
print(so.processTasks([[10,42,6],[47,81,35],[38,58,13],[39,48,4],[12,62,24],[54,73,1],[59,96,34],[65,91,20]]))  # 54
print(so.processTasks([[2,7,5],[3,5,1]]))  # 5





