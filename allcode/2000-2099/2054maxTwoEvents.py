# 给你一个下标从 0 开始的二维整数数组 events ，其中 events[i] = [startTimei, endTimei, valuei] 。第 i 个活动开始于 startTimei ，结束于 endTimei ，如果你参加这个活动，那么你可以得到价值 valuei 。你 最多 可以参加 两个时间不重叠 活动，使得它们的价值之和 最大 。
#
# 请你返回价值之和的 最大值 。
#
# 注意，活动的开始时间和结束时间是 包括 在活动时间内的，也就是说，你不能参加两个活动且它们之一的开始时间等于另一个活动的结束时间。更具体的，如果你参加一个活动，且结束时间为 t ，那么下一个活动必须在 t + 1 或之后的时间开始。
#
#
#
# 示例 1:
#
#
#
# 输入：events = [[1,3,2],[4,5,2],[2,4,3]]
# 输出：4
# 解释：选择绿色的活动 0 和 1 ，价值之和为 2 + 2 = 4 。
# 示例 2：
#
# Example 1 Diagram
#
# 输入：events = [[1,3,2],[4,5,2],[1,5,5]]
# 输出：5
# 解释：选择活动 2 ，价值和为 5 。
# 示例 3：
#
#
#
# 输入：events = [[1,5,3],[1,5,1],[6,6,5]]
# 输出：8
# 解释：选择活动 0 和 2 ，价值之和为 3 + 5 = 8 。
#
#
# 提示：
#
# 2 <= events.length <= 105
# events[i].length == 3
# 1 <= startTimei <= endTimei <= 109
# 1 <= valuei <= 106


from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort(key=lambda x:[x[1], -x[2]])
        end_max = [[events[0][1], events[0][2]]]  # [end, max]  # 结束时间<=end的最大价值
        for start, end, val in events[1:]:
            if end == end_max[-1][0]: continue
            end_max.append([end, max(val, end_max[-1][1])])
        events.sort(key=lambda x:[x[0], -x[2]])
        pos = 0
        ans = 0
        for start, end, val in events:
            while pos < n and end_max[pos][0] < start:
                pos += 1
            if pos == 0:
                ans = max(ans, val)
                continue
            ans = max(ans, val + end_max[pos - 1][1])
        return ans




so = Solution()
print(so.maxTwoEvents(events = [[10,83,53],[63,87,45],[97,100,32],[51,61,16]]))
print(so.maxTwoEvents(events = [[1,5,3],[1,5,1],[6,6,5]]))
print(so.maxTwoEvents(events = [[1,3,2],[4,5,2],[1,5,5]]))
print(so.maxTwoEvents(events = [[1,3,2],[4,5,2],[2,4,3]]))

