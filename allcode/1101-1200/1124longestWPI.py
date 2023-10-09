# 给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。
#
# 我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。
#
# 所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。
#
# 请你返回「表现良好时间段」的最大长度。
#
#
#
# 示例 1：
#
# 输入：hours = [9,9,6,0,6,6,9]
# 输出：3
# 解释：最长的表现良好时间段是 [9,9,6]。
# 示例 2：
#
# 输入：hours = [6,6,6]
# 输出：0
#
#
# 提示：
#
# 1 <= hours.length <= 104
# 0 <= hours[i] <= 16
from itertools import accumulate
from typing import List
from bisect import *
class Solution:
    def longestWPI1(self, hours: List[int]) -> int:
        hours = [1 if x > 8 else -1 for x in hours]
        pre_sum = [0]
        for x in hours:
            pre_sum.append(pre_sum[-1] + x)
        stack = [[0, 0]]
        ans = 0
        for i, x in enumerate(pre_sum):
            if -x > stack[-1][0]:
                stack.append([-x, i])
                continue
            elif -x == stack[-1][0]:
                continue
            pos = bisect_left(stack, -x, key=lambda y: y[0])
            if stack[pos][0] == -x:
                ans = max(ans, i - stack[pos + 1][1])
            else:
                ans = max(ans, i - stack[pos][1])
        return ans

    def longestWPI(self, hours: List[int]) -> int:
        hours = [1 if x > 8 else -1 for x in hours]
        s = list(accumulate(hours, initial=0))
        # 问题转换为求 s 的和为正数的最长子数组

        stack = [0]  # 单递减调栈中放的是所有可能成为最长序列的左端点的下标
        for i, x in enumerate(s[1:], 1):
            if stack and x < s[stack[-1]]:
                stack.append(i)
        n = len(s)
        ans = 0
        for i in range(n - 1, 0, -1):  # 对 s 逆序遍历，确定每 s[i] 能否成功最长子序列的右端点
            while stack and ((stack[-1] < i and s[stack[-1]] < s[i]) or stack[-1] == i):
            # while stack and s[stack[-1]] < s[i]:  # 可以简化为这个条件，但要思考一下
                ans = max(ans, i - stack.pop())
        return ans







obj = Solution()
print(obj.longestWPI([9,9,6,0,6,6,9]))  # 3
print(obj.longestWPI([6,9,9]))  # 3
print(obj.longestWPI([12,8,7,7,9,10,8,7,9,7,8,11]))  # 5
print(obj.longestWPI([6,6,6]))  # 0

