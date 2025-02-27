# 给你一个区间数组 intervals ，其中intervals[i] = [starti, endi] ，且每个starti 都 不同 。
#
# 区间 i 的 右侧区间 可以记作区间 j ，并满足 startj>= endi ，且 startj 最小化 。
#
# 返回一个由每个区间 i 的 右侧区间 在intervals 中对应下标组成的数组。如果某个区间 i 不存在对应的 右侧区间 ，则下标 i 处的值设为 -1 。
#
#
# 示例 1：
#
# 输入：intervals = [[1,2]]
# 输出：[-1]
# 解释：集合中只有一个区间，所以输出-1。
# 示例 2：
#
# 输入：intervals = [[3,4],[2,3],[1,2]]
# 输出：[-1,0,1]
# 解释：对于 [3,4] ，没有满足条件的“右侧”区间。
# 对于 [2,3] ，区间[3,4]具有最小的“右”起点;
# 对于 [1,2] ，区间[2,3]具有最小的“右”起点。
# 示例 3：
#
# 输入：intervals = [[1,4],[2,3],[3,4]]
# 输出：[-1,2,-1]
# 解释：对于区间 [1,4] 和 [3,4] ，没有满足条件的“右侧”区间。
# 对于 [2,3] ，区间 [3,4] 有最小的“右”起点。
#
#
# 提示：
#
# 1 <=intervals.length <= 2 * 104
# intervals[i].length == 2
# -106 <= starti <= endi <= 106
# 每个间隔的起点都 不相同




from leetcode.allcode.competition.mypackage import *

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        left = [e[0] for e in intervals]
        d = {e[0]: idx for idx, e in enumerate(intervals)}
        left.sort()
        res = []
        for v in intervals:
            if v[1] > left[-1]:
                res.append(-1)
            else:
                pos = bisect.bisect_left(left, v[1])
                res.append(d[left[pos]])
        return res



so = Solution()
print(so.findRightInterval([[1,2],[2,3],[0,1],[3,4]]))
print(so.findRightInterval([[3,4],[2,3],[1,2]]))
print(so.findRightInterval([[1,2]]))
print(so.findRightInterval([[1,4],[2,3],[3,4]]))
