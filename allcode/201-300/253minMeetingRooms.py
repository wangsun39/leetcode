# 给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，返回 所需会议室的最小数量 。
#
#
#
# 示例 1：
#
# 输入：intervals = [[0,30],[5,10],[15,20]]
# 输出：2
# 示例 2：
#
# 输入：intervals = [[7,10],[2,4]]
# 输出：1
#
#
# 提示：
#
# 1 <= intervals.length <= 104
# 0 <= starti < endi <= 106

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        diff = [0] * (10 ** 6 + 1)
        for x, y in intervals:
            diff[x] += 1
            diff[y + 1] -= 1
        s = list(accumulate(diff))
        return max(s)


so = Solution()
print(so.minMeetingRooms([[0,30],[5,10],[15,20]]))




