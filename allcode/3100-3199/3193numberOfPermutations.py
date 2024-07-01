# 给你一个整数 n 和一个二维数组 requirements ，其中 requirements[i] = [endi, cnti] 表示这个要求中的末尾下标和 逆序对 的数目。
#
# 整数数组 nums 中一个下标对 (i, j) 如果满足以下条件，那么它们被称为一个 逆序对 ：
#
# i < j 且 nums[i] > nums[j]
# 请你返回 [0, 1, 2, ..., n - 1] 的
# 排列
#  perm 的数目，满足对 所有 的 requirements[i] 都有 perm[0..endi] 恰好有 cnti 个逆序对。
#
# 由于答案可能会很大，将它对 109 + 7 取余 后返回。
#
#
#
# 示例 1：
#
# 输入：n = 3, requirements = [[2,2],[0,0]]
#
# 输出：2
#
# 解释：
#
# 两个排列为：
#
# [2, 0, 1]
# 前缀 [2, 0, 1] 的逆序对为 (0, 1) 和 (0, 2) 。
# 前缀 [2] 的逆序对数目为 0 个。
# [1, 2, 0]
# 前缀 [1, 2, 0] 的逆序对为 (0, 2) 和 (1, 2) 。
# 前缀 [1] 的逆序对数目为 0 个。
# 示例 2：
#
# 输入：n = 3, requirements = [[2,2],[1,1],[0,0]]
#
# 输出：1
#
# 解释：
#
# 唯一满足要求的排列是 [2, 0, 1] ：
#
# 前缀 [2, 0, 1] 的逆序对为 (0, 1) 和 (0, 2) 。
# 前缀 [2, 0] 的逆序对为 (0, 1) 。
# 前缀 [2] 的逆序对数目为 0 。
# 示例 3：
#
# 输入：n = 2, requirements = [[0,0],[1,0]]
#
# 输出：1
#
# 解释：
#
# 唯一满足要求的排列为 [0, 1] ：
#
# 前缀 [0] 的逆序对数目为 0 。
# 前缀 [0, 1] 的逆序对为 (0, 1) 。
#
#
#
# 提示：
#
# 2 <= n <= 300
# 1 <= requirements.length <= n
# requirements[i] = [endi, cnti]
# 0 <= endi <= n - 1
# 0 <= cnti <= 400
# 输入保证至少有一个 i 满足 endi == n - 1 。
# 输入保证所有的 endi 互不相同。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        requirements.sort()
        d = {k: v for k, v in requirements}
        if 0 in d and d[0] != 0: return 0
        m = requirements[-1][1]  # 最大逆序对数量
        dp = [[0] * (m + 1) for _ in range(n)]  # dp[i][j] 表示前 i 个数，逆序对的个数为 j 的排列数
        dp[0][0] = 1
        for i in range(1, n):
            for j in range(m + 1):
                if i in d and d[i] != j:
                    continue
                for k in range(max(0, j - i), j + 1):   # 第 i 个元素，最多能和前面的元素新产生 i 个逆序对，前面i-1个元素产生k个逆序对
                    # 则需要由第i个元素新产生 j-k 个逆序对，那么 0 <= j-k <= i，得 j-i<=k<=j
                    dp[i][j] += dp[i - 1][k]
                    dp[i][j] %= MOD
                if i in d and dp[i][j] == 0: return 0  # 不存在这样的排序
        # print(dp)
        return dp[-1][-1]



so = Solution()
print(so.numberOfPermutations(n = 2, requirements = [[0,0],[1,0]]))  # 1
print(so.numberOfPermutations(n = 3, requirements = [[2,2],[0,0]]))  # 2
print(so.numberOfPermutations(n = 15, requirements = [[4,5],[6,10],[14,53],[0,0]]))  # 393161917
print(so.numberOfPermutations(n = 3, requirements = [[2,2],[0,1]]))  # 0
print(so.numberOfPermutations(n = 3, requirements = [[2,2],[1,1],[0,0]]))  # 1




