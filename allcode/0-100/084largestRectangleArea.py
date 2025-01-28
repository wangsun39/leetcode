# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#
#
# 示例 1:
#
#
#
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
# 示例 2：
#
#
#
# 输入： heights = [2,4]
# 输出： 4
#
#
# 提示：
#
# 1 <= heights.length <=105
# 0 <= heights[i] <= 104


from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # heights.insert(0, 0)
        heights.append(0)
        N = len(heights)
        stack = [[-1, 0]]  # 第一个表示下标，第二个表示heights中对应的元素
        largest = [0] * N
        for i in range(N):
            # if stack[-1][1] <= heights[i]:
            #     stack.append([i, heights[i]])
            #     continue
            while stack[-1][1] > heights[i]:
                last_key, last_value = stack.pop()
                largest[last_key] = (i - stack[-1][0] - 1) * last_value
            stack.append([i, heights[i]])
        print(largest)
        return max(largest)

so = Solution()
print(so.largestRectangleArea([2,4]))
print(so.largestRectangleArea([2,1,5,6,2,3]))

