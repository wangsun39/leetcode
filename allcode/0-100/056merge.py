# 给出一个区间的集合，请合并所有重叠的区间。
#
# 
#
# 示例 1:
#
# 输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例2:
#
# 输入: intervals = [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。
#
# 
#
# 提示：
#
# intervals[i][0] <= intervals[i][1]
from leetcode.allcode.competition.mypackage import *
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 1:
            return []
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        print(intervals)
        for interval in intervals[1:]:
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)
        return res

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 2023/8/27
        intervals.sort()
        intervals.append([inf, inf])
        left, right = intervals[0]
        ans = []
        for x, y in intervals[1:]:
            if x > right:
                ans.append([left, right])
                left, right = x, y
                continue
            right = max(right, y)
        return ans

so = Solution()
print(so.merge([[1,4],[0,4]]))
print(so.merge([[1,3],[8,10],[15,18],[2,6]]))
