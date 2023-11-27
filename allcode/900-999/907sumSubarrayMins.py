# 给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。
#
# 由于答案可能很大，因此 返回答案模 10^9 + 7 。
#
#
#
# 示例 1：
#
# 输入：arr = [3,1,2,4]
# 输出：17
# 解释：
# 子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
# 最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
# 示例 2：
#
# 输入：arr = [11,81,94,43,3]
# 输出：444
#
#
# 提示：
#
# 1 <= arr.length <= 3 * 104
# 1 <= arr[i] <= 3 * 104

from typing import List
import bisect
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = arr[0]
        stack = [[arr[0], 1, arr[0]]]  # [a, b, c]  a - 最小值， b - 以a为最小值的区间和的个数，c - 前面所有最小值之和
        # s = [arr[0]]  # stack 的前缀和
        MOD = int(1e9 + 7)
        for i, e in enumerate(arr[1:], 1):
            cur = 0
            while len(stack) and stack[-1][0] >= e:
                cur += stack[-1][1]
                stack.pop()
            if len(stack):
                ans += stack[-1][2]
                ans %= MOD
                stack.append([e, cur + 1, stack[-1][2]])
            else:
                stack.append([e, cur + 1, 0])
            ans += stack[-1][0] * stack[-1][1]
            stack[-1][2] += stack[-1][0] * stack[-1][1]
            ans %= MOD
            # print(stack)
        return ans

    def sumSubarrayMins(self, arr: List[int]) -> int:
        # 2023/11/27 左右两边的分别单调栈 + 贡献法
        # 注意要考虑相等的值的处理
        MOD = 10 ** 9 + 7
        n = len(arr)
        left = [-1] * n  # 左侧第一个小于arr[i]的下标
        right = [n] * n  # 右侧第一个小于等于arr[i]的下标
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        ans = 0
        for i in range(n):
            ans += (i - left[i]) * (right[i] - i) * arr[i]
            ans %= MOD
        return ans



so = Solution()
print(so.sumSubarrayMins([3,1,2,4]))
print(so.sumSubarrayMins([11,81,94,43,3]))