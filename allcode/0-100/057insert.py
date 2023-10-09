# 给你一个 无重叠的 ，按照区间起始端点排序的区间列表。
#
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
#
#
#
# 示例 1：
#
# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]
# 示例 2：
#
# 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]
# 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
# 示例 3：
#
# 输入：intervals = [], newInterval = [5,7]
# 输出：[[5,7]]
# 示例 4：
#
# 输入：intervals = [[1,5]], newInterval = [2,3]
# 输出：[[1,5]]
# 示例 5：
#
# 输入：intervals = [[1,5]], newInterval = [2,7]
# 输出：[[1,7]]
#
#
# 提示：
#
# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= intervals[i][0] <= intervals[i][1] <= 105
# intervals 根据 intervals[i][0] 按 升序 排列
# newInterval.length == 2
# 0 <= newInterval[0] <= newInterval[1] <= 105

from bisect import bisect_left, bisect_right
from typing import List
class Solution:
    def insert1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def find(num):
            if intervals[N - 1][1] < num:
                return [N - 1, None]  # 位于所有区间的右边
            if intervals[0][0] > num:
                return [None, 0]  # 位于所有区间的左边
            if intervals[N - 1][0] <= num:
                return [N - 1]
            start, end = 0, N - 1
            while start < end - 1:
                idx = (start + end) // 2
                if intervals[idx][0] <= num:
                    start = idx
                else:
                    end = idx
            if intervals[start][1] < num:
                return [start, start + 1]  # 位于两个区间之间
            else:
                return [start]

        N = len(intervals)
        if 0 == N:
            return [newInterval]
        pos1 = find(newInterval[0])
        pos2 = find(newInterval[1])
        print(pos1)
        print(pos2)
        if pos1[0] is None:
            res = [newInterval]
        else:
            res = intervals[:pos1[0] + 1]
            if len(pos1) < 2:
                res[-1][1] = max(newInterval[1], res[-1][1])
            else:
                res.append(newInterval)
        if pos2[0] is None:
            return res + intervals
        if pos2[-1] is None:
            return res
        if len(pos2) < 2:
            res[-1][1] = intervals[pos2[0]][1]
        res += intervals[pos2[0] + 1:]
        return res

    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 2023/8/28  二分
        n = len(intervals)
        l, r = newInterval
        if n == 0 or l > intervals[-1][1]:
            return intervals + [newInterval]
        if r < intervals[0][0]:
            return [newInterval] + intervals
        p1 = bisect_left(intervals, l, key=lambda x:x[0])
        if p1 == n:
            return intervals[: -1] + [[intervals[-1][0], max(intervals[-1][1], r)]]
        if p1 == 0 or intervals[p1 - 1][1] < l:
            ans = intervals[: p1]
            left = l
        else:
            ans = intervals[: p1 - 1]
            left = intervals[p1 - 1][0]
        p2 = max(0, p1 - 1)
        right = intervals[p2][1]
        while p2 < n and r >= intervals[p2][0]:
            right = intervals[p2][1]
            p2 += 1
        right = max(right, r)
        ans.append([left, right])
        ans += intervals[p2:]
        return ans


    def insert3(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 2023/8/28  直接模拟
        n = len(intervals)
        l, r = newInterval
        p1 = 0
        ans = []
        while p1 < n and intervals[p1][1] < l:
            ans.append(intervals[p1])
            p1 += 1
        if p1 >= n or intervals[p1][0] > r:
            return ans + [newInterval] + intervals[p1:]
        left = min(l, intervals[p1][0])
        right = intervals[p1][1]
        while p1 < n and r >= intervals[p1][0]:
            right = intervals[p1][1]
            p1 += 1
        right = max(right, r)
        ans.append([left, right])
        ans += intervals[p1:]
        return ans

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 2023/8/29  二分
        n = len(intervals)
        l, r = newInterval
        if n == 0 or r < intervals[0][0]:
            return [newInterval] + intervals
        if l > intervals[-1][1]:
            return intervals + [newInterval]

        def find(x):  # 判断 x 是否落在某个区间上
            p = bisect_right(intervals, x, key=lambda x:x[0])
            if p == 0:
                return False, 0
            if intervals[p - 1][1] < x:
                return False, p  # 找不到返回，x右边的区间id
            return True, p - 1  # 找到，返回所属区间的id
        ans = []
        r1, p1 = find(l)
        r2, p2 = find(r)
        ans += intervals[: p1]
        if r1:
            left = intervals[p1][0]
        else:
            left = l
        if r2:
            right = intervals[p2][1]
            p2 += 1
        else:
            right = r
        ans.append([left, right])
        ans += intervals[p2:]

        return ans






so = Solution()
print(so.insert([[1,3],[6,9]], [2,5]))
print(so.insert( [[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
print(so.insert([[0,4],[7,12]], [0,5]))
print(so.insert([[0,5],[8,9]], [3,4]))
print(so.insert([[1,5]], [2,3]))
print(so.insert([[1,5]], [0,0]))
