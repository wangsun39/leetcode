# 给你一个二维整数数组intervals，其中intervals[i] = [lefti, righti]表示 闭区间[lefti, righti]。
#
# 你需要将intervals 划分为一个或者多个区间组，每个区间 只属于一个组，且同一个组中任意两个区间 不相交。
#
# 请你返回 最少需要划分成多少个组。
#
# 如果两个区间覆盖的范围有重叠（即至少有一个公共数字），那么我们称这两个区间是 相交的。比方说区间[1, 5] 和[5, 8]相交。
#
#
#
# 示例 1：
#
# 输入：intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
# 输出：3
# 解释：我们可以将区间划分为如下的区间组：
# - 第 1 组：[1, 5] ，[6, 8] 。
# - 第 2 组：[2, 3] ，[5, 10] 。
# - 第 3 组：[1, 10] 。
# 可以证明无法将区间划分为少于 3 个组。
# 示例 2：
#
# 输入：intervals = [[1,3],[5,6],[8,10],[11,13]]
# 输出：1
# 解释：所有区间互不相交，所以我们可以把它们全部放在一个组内。
#
#
# 提示：
#
# 1 <= intervals.length <= 105
# intervals[i].length == 2
# 1 <= lefti <= righti <= 106


from leetcode.allcode.competition.mypackage import *
# string.letters：包含所有字母(大写或小写字符串，在python3.0中，使用string.ascii-letters代替)
# string.lowercase：包含所有小写字母的字符串
# string.printable：包含所有可打印字符的字符串
# string.punctuation：包含所有标点的字符串
# string.uppercase：包含所有大写字母的字符串

class Solution:
    def minGroups1(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        group = [intervals[0][1]]
        for iv in intervals[1:]:
            if len(group) > 0 and group[0] < iv[0]:
                del(group[0])
                bisect.insort_right(group, iv[1])
            else:
                bisect.insort_right(group, iv[1])
        return len(group)

    def minGroups2(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = [intervals[0][1]]
        for it in intervals[1:]:
            if heap[0] >= it[0]:
                heapq.heappush(heap, it[1])
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, it[1])
        return len(heap)


    def minGroups(self, intervals: List[List[int]]) -> int:
        # 2023/9/19  差分数组
        mx = max(x[1] for x in intervals) + 1
        diff = [0] * mx
        for a, b in intervals:
            diff[a - 1] += 1
            diff[b] -= 1
        ans = cur = 0
        for x in diff:
            cur += x
            if cur > ans:
                ans = cur
        return ans

so = Solution()
print(so.minGroups([[1,3],[5,6],[8,10],[11,13]]))
print(so.minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))




