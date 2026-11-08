# 给你一个二维整数数组 meetings，其中 meetings[i] = [starti, endi, revenuei] 表示一场会议从时间 starti 开始，在时间 endi 结束，并可获得 revenuei 的收益。
#
# 所有会议均采用 左闭右开区间 [start, end) 表示，因此仅在端点处相接的会议 不视为 重叠。
#
# 你可以选择任意一个会议 非空子集 ，所选会议两两不重叠。每选择一场会议，你都可以获得该会议对应的收益。
#
# 将所选会议按照 开始时间递增 的顺序排列。对于该顺序中每一对相邻会议，你还可以根据它们之间的空闲时间获得额外收益，每单位空闲时间获得 1 单位收益。空闲时间等于后一场会议的开始时间减去前一场会议的结束时间。
#
# 最早一场所选会议开始之前，以及最晚一场所选会议结束之后的空闲时间不会产生收益。如果只选择一场会议，则不会获得任何空闲时间收益。
#
# 返回可以获得的 最大总收益 。
#
# 数组的 子集 是从数组中选择若干元素得到的集合。
#
#
#
# 示例 1：
#
# 输入： meetings = [[2,5,4],[6,8,3]]
#
# 输出： 8
#
# 解释：
#
# 选择两场会议。它们互不重叠，会议收益为 4 + 3 = 7。
# 第一场会议在时间 5 结束，第二场会议在时间 6 开始，因此中间的空闲时间可额外获得 6 - 5 = 1 单位收益。
# 最大总收益为 7 + 1 = 8。
# 示例 2：
#
# 输入： meetings = [[3,5,4],[4,7,8],[8,10,3]]
#
# 输出： 12
#
# 解释：
#
# 选择下标为 1 和 2 的会议。它们互不重叠，会议收益为 8 + 3 = 11。
# 按时间顺序，这两场会议分别从时间 4 到 7、从时间 8 到 10。中间的空闲时间可额外获得 8 - 7 = 1 单位收益。
# 最大总收益为 11 + 1 = 12。
# 示例 3：
#
# 输入： meetings = [[1,2,2],[4,5,2],[7,9,3]]
#
# 输出： 11
#
# 解释：
#
# 选择全部三场会议。它们互不重叠，会议收益为 2 + 2 + 3 = 7。
# 从时间 2 到 4 的空闲时间可额外获得 4 - 2 = 2 单位收益。
# 从时间 5 到 7 的空闲时间可额外获得 7 - 5 = 2 单位收益。
# 最大总收益为 7 + 2 + 2 = 11。
#
#
# 提示
# 1 <= meetings.length <= 105
# meetings[i] = [starti, endi, revenuei]
# 0 <= starti < endi <= 109
# 1 <= revenuei <= 109

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a


class Solution:
    def maxEarnings(self, meetings: list[list[int]]) -> int:
        meetings.sort(key=lambda x: x[1])
        # 令 r[i] 是以第i个会议为最后一个会议时的最大收入
        # 则， 对于 i < j， 如果r[i]+end[j]-end[i]>=r[j]  就没有必要选第j个会议作为结束，因为如果选择了某个 晚于i，j的会议时，能同时选j会议，一定也能选i会议
        # 而且不选j会议的收益小于选择j会议的收益
        # 此时j会议在后续就不需要考虑，不用放入单调栈
        # 而 r[i]+end[j]-end[i]<r[j] 时，i和j都是有可能在后续选择中使用，可以直接放入单调栈
        # 式子变形: r[i]-end[i]<r[j]-end[j]  这就满足一个单调增的数据结构
        stack = []  #  [a, c]  a: 为 meetings 的一个下标， b: 以 meetings[a][1] 时间结束的会议，结束时最大的收益
        # c: b - meetings[a][1]
        ans = 0
        for i, [x, y, r] in enumerate(meetings):
            p = bisect_right(stack, x, key=lambda y: meetings[y[0]][1])   # 单调栈中找一个结束时间小于x的位置， meetings[y[0]][1] 是栈中元素的结束时间
            v = 0  # 以当前会议结束的最大收益
            if p == 0:
                # 作为第一个会议
                v = r
            else:
                # 前面允许的会议的最大收益 stack[p][1] + meetings[stack[p][0]][1]
                pre = meetings[stack[p - 1][0]][1]  # 前一个会议的结束时间
                v = stack[p - 1][1] + pre + r + x - pre
            ans = MAX(ans, v)
            # 尝试是否能放入单调栈
            if not stack or stack[-1][1] < v - y:
                stack.append([i, v - y])
        return ans





so = Solution()
print(so.maxEarnings(meetings = [[7,13,10],[4,7,8]]))
print(so.maxEarnings(meetings = [[3,5,4],[4,7,8],[8,10,3]]))
print(so.maxEarnings(meetings = [[2,5,4],[6,8,3]]))



