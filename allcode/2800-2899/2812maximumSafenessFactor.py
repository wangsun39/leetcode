# 给你一个下标从 0 开始长度为 n 的数组 nums 。
#
# 每一秒，你可以对数组执行以下操作：
#
# 对于范围在 [0, n - 1] 内的每一个下标 i ，将 nums[i] 替换成 nums[i] ，nums[(i - 1 + n) % n] 或者 nums[(i + 1) % n] 三者之一。
# 注意，所有元素会被同时替换。
#
# 请你返回将数组 nums 中所有元素变成相等元素所需要的 最少 秒数。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,1,2]
# 输出：1
# 解释：我们可以在 1 秒内将数组变成相等元素：
# - 第 1 秒，将每个位置的元素分别变为 [nums[3],nums[1],nums[3],nums[3]] 。变化后，nums = [2,2,2,2] 。
# 1 秒是将数组变成相等元素所需要的最少秒数。
# 示例 2：
#
# 输入：nums = [2,1,3,3,2]
# 输出：2
# 解释：我们可以在 2 秒内将数组变成相等元素：
# - 第 1 秒，将每个位置的元素分别变为 [nums[0],nums[2],nums[2],nums[2],nums[3]] 。变化后，nums = [2,3,3,3,3] 。
# - 第 2 秒，将每个位置的元素分别变为 [nums[1],nums[1],nums[2],nums[3],nums[4]] 。变化后，nums = [3,3,3,3,3] 。
# 2 秒是将数组变成相等元素所需要的最少秒数。
# 示例 3：
#
# 输入：nums = [5,5,5,5]
# 输出：0
# 解释：不需要执行任何操作，因为一开始数组中的元素已经全部相等。
#
#
# 提示：
#
# 1 <= n == nums.length <= 105
# 1 <= nums[i] <= 109

from leetcode.allcode.competition.mypackage import *


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        s = set()
        hi = inf
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    s.add((i, j))
                    hi = min(hi, i + j)
                    hi = min(hi, n - 1 - i + n - 1 - j)

        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def getAll(val):  # 找到所有到小偷距离小于 val 的点
            if val < 0: return set()
            dq = deque(x for x in s)
            res = set(x for x in s)
            step = 0
            while dq:
                dq2 = deque()
                step += 1
                if step >= val:
                    break
                while dq:
                    x, y = dq.popleft()
                    for dx, dy in dir:
                        u, v = x + dx, y + dy
                        if 0 <= u < n and 0 <= v < n and (u, v) not in res:
                            dq2.append((u, v))
                            res.add((u, v))
                dq = dq2
            return res

        def check(val):
            vis = getAll(val)
            if (0, 0) in vis:
                return False

            dq = deque([(0, 0)])
            vis.add((0, 0))
            while dq:
                x, y = dq.popleft()
                for dx, dy in dir:
                    u, v = x + dx, y + dy
                    if 0 <= u < n and 0 <= v < n and (u, v) not in vis:
                        if u == v == n - 1:
                            return True
                        dq.append((u, v))
                        vis.add((u, v))
            return False
        lo, hi = 0, hi + 1
        while lo < hi - 1:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid
        return lo

so = Solution()
print(so.maximumSafenessFactor(grid = [[0,0,1],[0,0,0],[0,0,0]]))
print(so.maximumSafenessFactor(grid = [[1,0,0],[0,0,0],[0,0,1]]))
print(so.maximumSafenessFactor(grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]))




