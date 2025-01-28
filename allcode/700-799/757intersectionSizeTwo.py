# 一个整数区间[a, b](a < b) 代表着从a到b的所有连续整数，包括a和b。
#
# 给你一组整数区间intervals，请找到一个最小的集合 S，使得 S 里的元素与区间intervals中的每一个整数区间都至少有2个元素相交。
#
# 输出这个最小集合S的大小。
#
# 示例 1:
#
# 输入: intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
# 输出: 3
# 解释:
# 考虑集合 S = {2, 3, 4}. S与intervals中的四个区间都有至少2个相交的元素。
# 且这是S最小的情况，故我们输出3。
# 示例 2:
#
# 输入: intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
# 输出: 5
# 解释:
# 最小的集合S = {1, 2, 3, 4, 5}.
# 注意:
#
# intervals的长度范围为[1, 3000]。
# intervals[i]长度为2，分别代表左、右边界。
# intervals[i][j] 的值是[0, 10^8]范围内的整数。


from typing import List
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:[x[1], -x[0]])
        print(intervals)
        x, y = intervals[0][1] - 1, intervals[0][1]
        ans = [x, y]
        for intv in intervals[1:]:
            if intv[0] <= x:
                continue
            if intv[0] <= y:
                x, y = y, intv[1]
                ans.append(y)
            else:
                x, y = intv[1] - 1, intv[1]
                ans += [x, y]

        return len(ans)



so = Solution()
print(so.intersectionSizeTwo([[1, 2], [2, 3], [2, 4], [4, 5]]))
print(so.intersectionSizeTwo([[1, 3], [1, 4], [2, 5], [3, 5]]))

