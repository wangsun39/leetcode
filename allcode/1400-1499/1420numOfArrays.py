# 给定三个整数 n、m 和 k 。考虑使用下图描述的算法找出正整数数组中最大的元素。
#
#
#
# 请你构建一个具有以下属性的数组 arr ：
#
# arr 中包含确切的 n 个整数。
# 1 <= arr[i] <= m 其中 (0 <= i < n) 。
# 将上面提到的算法应用于 arr 之后，search_cost 的值等于 k 。
# 返回在满足上述条件的情况下构建数组 arr 的 方法数量 ，由于答案可能会很大，所以 必须 对 10^9 + 7 取余。
#
#
#
# 示例 1：
#
# 输入：n = 2, m = 3, k = 1
# 输出：6
# 解释：可能的数组分别为 [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
# 示例 2：
#
# 输入：n = 5, m = 2, k = 3
# 输出：0
# 解释：没有数组可以满足上述条件
# 示例 3：
#
# 输入：n = 9, m = 1, k = 1
# 输出：1
# 解释：唯一可能的数组是 [1, 1, 1, 1, 1, 1, 1, 1, 1]
#
#
# 提示：
#
# 1 <= n <= 50
# 1 <= m <= 100
# 0 <= k <= n

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def dfs(idx, mx, tm):  # 从数组的第i的元素开始，前面的元素最大值为mx，前面的元素已经递增了tm次
            if k < tm: return 0
            if n - idx < k - tm:
                return 0
            if m - mx < k - tm:
                return 0
            if idx == n:
                return 1
            res = dfs(idx + 1, mx, tm) * mx
            res %= MOD
            for i in range(mx + 1, m + 1):
                res += dfs(idx + 1, i, tm + 1)
                res %= MOD
            return res
        return dfs(0, 0, 0)

so = Solution()
print(so.numOfArrays(n = 2, m = 3, k = 1))  # 6
print(so.numOfArrays(n = 2, m = 2, k = 1))  # 3
print(so.numOfArrays(n = 1, m = 1, k = 1))  # 1
print(so.numOfArrays(n = 5, m = 2, k = 3))  # 0
print(so.numOfArrays(n = 9, m = 1, k = 1))  # 1




