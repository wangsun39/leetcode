# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
#
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
#
#  
#
# 示例 1：
#
# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]
# 示例 2：
#
# 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]
# 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。


from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
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





so = Solution()
print(so.insert([[1,5]], [0,0]))
print(so.insert([[1,5]], [2,3]))
print(so.insert([[1,3],[6,9]], [2,5]))
print(so.insert( [[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
