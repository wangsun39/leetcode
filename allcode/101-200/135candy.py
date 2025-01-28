# n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
#
# 你需要按照以下要求，给这些孩子分发糖果：
#
# 每个孩子至少分配到 1 个糖果。
# 相邻两个孩子评分更高的孩子会获得更多的糖果。
# 请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。
#
# 
#
# 示例1：
#
# 输入：ratings = [1,0,2]
# 输出：5
# 解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。
# 示例2：
#
# 输入：ratings = [1,2,2]
# 输出：4
# 解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
#      第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。
# 
#
# 提示：
#
# n == ratings.length
# 1 <= n <= 2 * 104
# 0 <= ratings[i] <= 2 * 104
#
# https://leetcode.cn/problems/candy

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ratings.insert(0, -1)
        rs = [[r, i] for i, r in enumerate(ratings)]
        rs.sort()
        rs.append([-1, n + 1])
        dispatch = [0] * (n + 2)
        for val, idx in rs[1: n + 1]:
            l = dispatch[idx - 1]
            r = dispatch[idx + 1]
            if l == 0 and r == 0:
                dispatch[idx] = 1
                continue
            if l > 0:
                if val > ratings[idx - 1]:
                    dispatch[idx] = max(dispatch[idx], dispatch[idx - 1] + 1)
                else:
                    dispatch[idx] = max(dispatch[idx], 1)
            if r > 0:
                if val > ratings[idx + 1]:
                    dispatch[idx] = max(dispatch[idx], dispatch[idx + 1] + 1)
                else:
                    dispatch[idx] = max(dispatch[idx], 1)
        print(dispatch)

        return sum(dispatch)


so = Solution()
print(so.candy([1,0,2]))
print(so.candy([1,2,2]))


