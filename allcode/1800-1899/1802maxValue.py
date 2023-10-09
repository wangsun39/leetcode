# 给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：
#
# nums.length == n
# nums[i] 是 正整数 ，其中 0 <= i < n
# abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1
# nums 中所有元素之和不超过 maxSum
# nums[index] 的值被 最大化
# 返回你所构造的数组中的 nums[index] 。
#
# 注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。
#
#
#
# 示例 1：
#
# 输入：n = 4, index = 2,  maxSum = 6
# 输出：2
# 解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。
# 示例 2：
#
# 输入：n = 6, index = 1,  maxSum = 10
# 输出：3
#
#
# 提示：
#
# 1 <= n <= maxSum <= 109
# 0 <= index < n


from typing import List
import heapq

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        lo, hi = (maxSum + n - 1) // n, maxSum + 1
        index += 1  # 变换为下标从 1 到 n
        def judge(x):
            if x >= index:
                left = x * index - index * (index - 1) // 2  # nums 从 1 到 index 项之和
            else:
                left = (x + 1) * x // 2 + (index - x)
            if n - index + 1 <= x:
                right = (x - 1) * (n - index) - (n - index) * (n - index - 1) // 2  # nums 从 index 到 最后一项之和
            else:
                right = (x - 1) * x // 2 + (n - index) - (x - 1)
            return left + right <= maxSum
        while lo < hi - 1:  # 始终保证 lo 是满足的，hi 是不满足的
            mid = (lo + hi) // 2
            if judge(mid):
                lo = mid
            else:
                hi = mid
        return lo


so = Solution()

print(so.maxValue(n = 1, index = 0,  maxSum = 24))
print(so.maxValue(n = 6, index = 1,  maxSum = 10))
print(so.maxValue(n = 4, index = 2,  maxSum = 6))




