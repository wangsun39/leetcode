# 给你一个整数 eventTime 表示一个活动的总时长，这个活动开始于 t = 0 ，结束于 t = eventTime 。
#
# 同时给你两个长度为 n 的整数数组 startTime 和 endTime 。它们表示这次活动中 n 个时间 没有重叠 的会议，其中第 i 个会议的时间为 [startTime[i], endTime[i]] 。
#
# 你可以重新安排 至多 一个会议，安排的规则是将会议时间平移，且保持原来的 会议时长 ，你的目的是移动会议后 最大化 相邻两个会议之间的 最长 连续空余时间。
#
# 请你返回重新安排会议以后，可以得到的 最大 空余时间。
#
# 注意，会议 不能 安排到整个活动的时间以外，且会议之间需要保持互不重叠。
#
# 注意：重新安排会议以后，会议之间的顺序可以发生改变。
#
#
#
# 示例 1：
#
# 输入：eventTime = 5, startTime = [1,3], endTime = [2,5]
#
# 输出：2
#
# 解释：
#
#
#
# 将 [1, 2] 的会议安排到 [2, 3] ，得到空余时间 [0, 2] 。
#
# 示例 2：
#
# 输入：eventTime = 10, startTime = [0,7,9], endTime = [1,8,10]
#
# 输出：7
#
# 解释：
#
#
#
# 将 [0, 1] 的会议安排到 [8, 9] ，得到空余时间 [0, 7] 。
#
# 示例 3：
#
# 输入：eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10]
#
# 输出：6
#
# 解释：
#
#
#
# 将 [3, 4] 的会议安排到 [8, 9] ，得到空余时间 [1, 7] 。
#
# 示例 4：
#
# 输入：eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]
#
# 输出：0
#
# 解释：
#
# 活动中的所有时间都被会议安排满了。
#
#
#
# 提示：
#
# 1 <= eventTime <= 109
# n == startTime.length == endTime.length
# 2 <= n <= 105
# 0 <= startTime[i] < endTime[i] <= eventTime
# endTime[i] <= startTime[i + 1] 其中 i 在范围 [0, n - 2] 之间。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        intv1 = []  # 所有间隔和会议时长按顺序的数组
        intv2 = []  # 所有间隔的数组
        intv1.append(startTime[0] - 0)
        intv2.append(startTime[0] - 0)
        for i in range(n - 1):
            intv1.append(endTime[i] - startTime[i])
            intv1.append(startTime[i + 1] - endTime[i])
            intv2.append(startTime[i + 1] - endTime[i])
        intv1.append(endTime[-1] - startTime[-1])
        intv1.append(eventTime - endTime[-1])
        intv2.append(eventTime - endTime[-1])
        if len(intv1) == 0: return 0
        intv2.sort()
        ans = 0
        for i in range(1, len(intv1), 2):
            x = intv1[i]  # 会议的时长
            pre = intv1[i - 1]
            later = intv1[i + 1]
            ans = max(ans, pre + later)
            p = bisect_left(intv2, x)  # 是否有一个间隔能放下这个会议
            v = 0  # 统计当前会议的前后间隔是否有超过会议时长的间隔
            if pre >= x: v += 1
            if later >= x: v += 1
            if len(intv2) - p - v > 0:  # 不能算当前会议的前后间隔，要去掉v个间隔
                ans = max(ans, pre + later + x)
        return ans

so = Solution()
print(so.maxFreeTime(eventTime = 52, startTime = [28,38], endTime = [38,41]))
print(so.maxFreeTime(eventTime = 5, startTime = [1,3], endTime = [2,5]))
print(so.maxFreeTime(eventTime = 10, startTime = [0,7,9], endTime = [1,8,10]))




