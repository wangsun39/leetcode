# 现有一份 n + m次投掷单个 六面 骰子的观测数据，骰子的每个面从 1 到 6 编号。观测数据中缺失了 n 份，你手上只拿到剩余m 次投掷的数据。幸好你有之前计算过的这 n + m 次投掷数据的 平均值 。
#
# 给你一个长度为 m 的整数数组 rolls ，其中rolls[i] 是第 i 次观测的值。同时给你两个整数 mean 和 n 。
#
# 返回一个长度为 n 的数组，包含所有缺失的观测数据，且满足这 n + m 次投掷的 平均值 是 mean 。如果存在多组符合要求的答案，只需要返回其中任意一组即可。如果不存在答案，返回一个空数组。
#
# k个数字的 平均值 为这些数字求和后再除以k 。
#
# 注意 mean 是一个整数，所以 n + m 次投掷的总和需要被n + m整除。
#
#
#
# 示例 1：
#
# 输入：rolls = [3,2,4,3], mean = 4, n = 2
# 输出：[6,6]
# 解释：所有 n + m 次投掷的平均值是 (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4 。
# 示例 2：
#
# 输入：rolls = [1,5,6], mean = 3, n = 4
# 输出：[2,3,2,2]
# 解释：所有 n + m 次投掷的平均值是 (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3 。
# 示例 3：
#
# 输入：rolls = [1,2,3,4], mean = 6, n = 4
# 输出：[]
# 解释：无论丢失的 4 次数据是什么，平均值都不可能是 6 。
# 示例 4：
#
# 输入：rolls = [1], mean = 3, n = 1
# 输出：[5]
# 解释：所有 n + m 次投掷的平均值是 (1 + 5) / 2 = 3 。
#
#
# 提示：
#
# m == rolls.length
# 1 <= n, m <= 105
# 1 <= rolls[i], mean <= 6




from leetcode.allcode.competition.mypackage import *
# Definition for a binary tree node.
class Solution:
    def missingRolls1(self, rolls: List[int], mean: int, n: int) -> List[int]:
        def helper(left, total, target):  # total 剩下可选的数字个数，target 数字之和
            if target == 0:
                return True, [0 for _ in range(len(left))]
            if len(left) == 0 or left[0] * total > target or left[-1] * total < target:
                return False, []
            num = 0
            while True:
                ans = helper(left[1:], total - num, target - num * left[0])
                if ans[0]:
                    return True, [num] + ans[1]
                num += 1
                if num > target:
                    return False, []
        m = len(rolls)
        left = [1, 2, 3, 4, 5, 6]
        target = mean * (m + n) - sum(rolls)
        ans = helper(left, n, target)
        if not ans[0]:
            return []
        res = []
        for i, num in enumerate(ans[1]):
            res += ([i + 1] * num)
        return res

    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # 2024/5/27  数学
        m = len(rolls)
        total = (m + n) * mean
        left = total - sum(rolls)
        if n <= left <= n * 6:
            q, r = divmod(left, n)
            ans = [q] * (n - r) + [q + 1] * r
            return ans
        return []



so = Solution()
print(so.missingRolls([3,2,4,3], mean = 4, n = 2))
print(so.missingRolls([1,2,3,4], mean = 6, n = 4))
print(so.missingRolls([1], mean = 3, n = 1))




