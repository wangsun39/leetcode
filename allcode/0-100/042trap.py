# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#  
#
# 示例 1：
#
#
#
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
# 示例 2：
#
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#  
#
# 提示：
#
# n == height.length
# 0 <= n <= 3 * 104
# 0 <= height[i] <= 105


from typing import List
from collections import deque

class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        res = 0
        if N < 3:
            return 0
        highest = 0
        if height[0] < height[1]:
            highest = 1

        # 思路：从左至右依次遍历，到某个柱子后，直接计算当前最大储水量，然后将储水位置全部“填平”，继续计算
        for i in range(1, N):
            if height[i] > height[i - 1]:
                waterLevel = min(height[highest], height[i])
                res += sum([waterLevel - e if waterLevel > e else 0 for e in height[highest + 1: i]])
                for j in range(highest + 1, i):
                    height[j] = max(waterLevel, height[j])
            if height[i] >= height[highest]:
                highest = i
        return res

    def trap(self, height: List[int]) -> int:
        # 2023/3/6 单调栈方法
        stack = deque([[height[0], 0]])  # 单调递减栈
        ans = 0
        for i, x in enumerate(height[1:], 1):
            base = -1
            if stack[-1][0] < x:
                base = stack[-1][0]

            while len(stack) and stack[-1][0] <= x:
                y, j = stack.pop()
                ans += (y - base) * (i - j - 1)  # 增加 高度差 * 宽度
                base = y
            if len(stack) and base != -1:
                ans += (x - base) * (i - stack[-1][1] - 1)
            stack.append([x, i])
        return ans


so = Solution()

print(so.trap([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]))   # 83
print(so.trap([5,4,1,2]))   # 1
print(so.trap([0,1,0,2,1,0,1,3,2,1,2,1]))   # 6
print(so.trap([4,2,0,3,2,5]))   # 9
