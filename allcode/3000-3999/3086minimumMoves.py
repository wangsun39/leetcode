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
        ones = [i for i, x in enumerate(nums) if x == 1]
        s = list(accumulate(ones, initial=0))
        left = SortedList()
        right = SortedList()
        n = len(nums)
        if n > 3:
            right = SortedList(i for i in range(3, n) if nums[i] == 1)

        def get(p, v):  # 计算以p为index，使用方法二的动作，最多的动作次数
            lo, hi = 1, 10 ** 5 + 1
            while lo < hi - 1:
                mid = (lo + hi) // 2
                pl = left.bisect_right(-p - mid)
                pr = right.bisect_right(p + mid)
                if pl + pr >= v:
                    hi = mid
                else:
                    lo = mid
            # hi 是向两侧最远的需要交换的距离
            pl = left.bisect_right(-p - hi)
            pr = right.bisect_right(p + hi)
            if pl + pr == v:
                idl = -left[pl] if pl < len(left) else 0
                idr = right[pr] if pr < len(right) else n - 1
                lact = s[p - 2] - s[idl]
                ract = s[idr + 1] - s[p + 3]
                return lact + ract
            lact = s[p] - s[-left[pl]]
            ract = s[p + pr - 1] - s[p]
            return lact + ract
        def calc(p):
            act = got = 0  # got是拾到1的个数，act是行动次数
            if nums[p] == 1:
                got = 1
            if got >= k: return act
            if p > 0 and nums[p - 1] == 1:
                act += 1
                got += 1
            if got >= k: return act
            if p < n - 1 and nums[p + 1] == 1:
                act += 1
                got += 1
            if got >= k: return act
            if p > 1 and nums[p - 2] == 1:
                act += 2
                got += 1
            if got >= k: return act
            if p < n - 2 and nums[p + 2] == 1:
                act += 2
                got += 1
            if got >= k: return act
            if got + maxChanges >= k:
                return got + (k - got) * 2
            act += maxChanges * 2
            got += maxChanges
            return act + get(p, k - got)

        ans = inf
        for pos in range(n):  # 枚举index位置
            if pos > 0:
                if right and right[0] <= pos + 2:
                    right.pop(0)
                if pos - 3 >= 0 and nums[pos - 3] == 1:
                    left.add(-(pos - 3))
            ans = min(ans, calc(pos))
        return ans


so = Solution()
print(so.minimumMoves(nums = [1,1,0,0,0,1,1,0,0,1], k = 3, maxChanges = 1))




