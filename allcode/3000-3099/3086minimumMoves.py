# 给你一个下标从 0 开始的二进制数组 nums，其长度为 n ；另给你一个 正整数 k 以及一个 非负整数 maxChanges 。
#
# Alice 在玩一个游戏，游戏的目标是让 Alice 使用 最少 数量的 行动 次数从 nums 中拾起 k 个 1 。游戏开始时，Alice 可以选择数组 [0, n - 1] 范围内的任何索引 aliceIndex 站立。如果 nums[aliceIndex] == 1 ，Alice 会拾起一个 1 ，并且 nums[aliceIndex] 变成0（这 不算 作一次行动）。之后，Alice 可以执行 任意数量 的 行动（包括零次），在每次行动中 Alice 必须 恰好 执行以下动作之一：
#
# 选择任意一个下标 j != aliceIndex 且满足 nums[j] == 0 ，然后将 nums[j] 设置为 1 。这个动作最多可以执行 maxChanges 次。
# 选择任意两个相邻的下标 x 和 y（|x - y| == 1）且满足 nums[x] == 1, nums[y] == 0 ，然后交换它们的值（将 nums[y] = 1 和 nums[x] = 0）。如果 y == aliceIndex，在这次行动后 Alice 拾起一个 1 ，并且 nums[y] 变成 0 。
# 返回 Alice 拾起 恰好 k 个 1 所需的 最少 行动次数。
#
#
#
# 示例 1：
#
# 输入：nums = [1,1,0,0,0,1,1,0,0,1], k = 3, maxChanges = 1
#
# 输出：3
#
# 解释：如果游戏开始时 Alice 在 aliceIndex == 1 的位置上，按照以下步骤执行每个动作，他可以利用 3 次行动拾取 3 个 1 ：
#
# 游戏开始时 Alice 拾取了一个 1 ，nums[1] 变成了 0。此时 nums 变为 [1,1,1,0,0,1,1,0,0,1] 。
# 选择 j == 2 并执行第一种类型的动作。nums 变为 [1,0,1,0,0,1,1,0,0,1]
# 选择 x == 2 和 y == 1 ，并执行第二种类型的动作。nums 变为 [1,1,0,0,0,1,1,0,0,1] 。由于 y == aliceIndex，Alice 拾取了一个 1 ，nums 变为  [1,0,0,0,0,1,1,0,0,1] 。
# 选择 x == 0 和 y == 1 ，并执行第二种类型的动作。nums 变为 [0,1,0,0,0,1,1,0,0,1] 。由于 y == aliceIndex，Alice 拾取了一个 1 ，nums 变为  [0,0,0,0,0,1,1,0,0,1] 。
# 请注意，Alice 也可能执行其他的 3 次行动序列达成拾取 3 个 1 。
#
# 示例 2：
#
# 输入：nums = [0,0,0,0], k = 2, maxChanges = 3
#
# 输出：4
#
# 解释：如果游戏开始时 Alice 在 aliceIndex == 0 的位置上，按照以下步骤执行每个动作，他可以利用 4 次行动拾取 2 个 1 ：
#
# 选择 j == 1 并执行第一种类型的动作。nums 变为 [0,1,0,0] 。
# 选择 x == 1 和 y == 0 ，并执行第二种类型的动作。nums 变为 [1,0,0,0] 。由于 y == aliceIndex，Alice 拾起了一个 1 ，nums 变为 [0,0,0,0] 。
# 再次选择 j == 1 并执行第一种类型的动作。nums 变为 [0,1,0,0] 。
# 再次选择 x == 1 和 y == 0 ，并执行第二种类型的动作。nums 变为 [1,0,0,0] 。由于y == aliceIndex，Alice 拾起了一个 1 ，nums 变为 [0,0,0,0] 。
#
#
# 提示：
#
# 2 <= n <= 105
# 0 <= nums[i] <= 1
# 1 <= k <= 105
# 0 <= maxChanges <= 105
# maxChanges + sum(nums) >= k

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        c = 0  # 对于连续的3个位置，最多有几个连续1
        n = len(nums)
        for i in range(n):
            s = sum(nums[i: min(n, i + 3)])
            if s == 3:
                c = 3
                break
            if s == 2:
                if nums[i + 1] != 0:
                    c = max(c, 2)
                else:
                    c = max(c, 1)
            elif s == 1:
                c = max(c, 1)
        if c >= k:
            return k - 1
        if maxChanges + c >= k:
            return max(0, c - 1) + (k - c) * 2

        # 剩下的又要用到第二种操作
        # 优先用的是maxChange，剩下的就变成货仓选址问题，计算过程自然会对连续的3个位置进行不超过2次拾起全部1的操作
        # 因此不需要先进行连续3个位置的计算
        idx = [i for i, x in enumerate(nums) if x]
        s = list(accumulate(idx, initial=0))
        m = len(idx)
        ans = inf
        # 在idx中选连续 k - maxChange 个 1，将其都移到中位数处
        for i in range(m - (k - maxChanges) + 1):
            # 子数组 idx[i: i + k - maxChanges]
            if (k - maxChanges) & 1:  # 长度为奇数
                mid = i + (k - maxChanges) // 2
                s1 = s[mid] - s[0]
                s2 = s[i + k - maxChanges] - s[mid + 1]
            else:
                mid = i + (k - maxChanges) // 2
                s1 = s[mid] - s[0]
                s2 = s[i + k - maxChanges] - s[mid]
            ans = min(ans, s2 - s1)
        return ans + maxChanges * 2





so = Solution()
print(so.minimumMoves(nums = [0,1,1,0,1,0,1,0,1], k = 8, maxChanges = 5))  # 13
print(so.minimumMoves(nums = [0,0,1,1], k = 2, maxChanges = 6))  # 1
print(so.minimumMoves(nums = [1,1], k = 3, maxChanges = 2))  # 3
print(so.minimumMoves(nums = [1,0,1], k = 2, maxChanges = 0))   # 2
print(so.minimumMoves(nums = [1,0,1,0,1], k = 3, maxChanges = 0))   # 4
print(so.minimumMoves(nums = [1,1], k = 1, maxChanges = 2))   # 0
print(so.minimumMoves(nums = [0,1], k = 1, maxChanges = 2))  # 0
print(so.minimumMoves(nums = [0,0,0,0], k = 2, maxChanges = 3))  # 4
print(so.minimumMoves(nums = [1,1,0,0,0,1,1,0,0,1], k = 3, maxChanges = 1))  # 3




