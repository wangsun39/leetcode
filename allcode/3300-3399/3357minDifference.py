# 给你一个整数数组 nums 。nums 中的一些值 缺失 了，缺失的元素标记为 -1 。
#
# 你需要选择 一个正 整数数对 (x, y) ，并将 nums 中每一个 缺失 元素用 x 或者 y 替换。
#
# 你的任务是替换 nums 中的所有缺失元素，最小化 替换后数组中相邻元素 绝对差值 的 最大值 。
#
# 请你返回上述要求下的 最小值 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,-1,10,8]
#
# 输出：4
#
# 解释：
#
# 选择数对 (6, 7) ，nums 变为 [1, 2, 6, 10, 8] 。
#
# 相邻元素的绝对差值分别为：
#
# |1 - 2| == 1
# |2 - 6| == 4
# |6 - 10| == 4
# |10 - 8| == 2
# 示例 2：
#
# 输入：nums = [-1,-1,-1]
#
# 输出：0
#
# 解释：
#
# 选择数对 (4, 4) ，nums 变为 [4, 4, 4] 。
#
# 示例 3：
#
# 输入：nums = [-1,10,-1,8]
#
# 输出：1
#
# 解释：
#
# 选择数对 (11, 9) ，nums 变为 [11, 10, 9, 8] 。
#
#
#
# 提示：
#
# 2 <= nums.length <= 105
# nums[i] 要么是 -1 ，要么是范围 [1, 109] 中的一个整数。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if all(x == -1 for x in nums): return 0
        lo = -inf
        for x, y in pairwise(nums):
            if x != -1 and y != -1:
                lo = max(lo, abs(x - y))
        if lo == -inf:
            lo = 0
        mx, mn = 0, inf  # 与 -1 相邻的最大最小值
        for i in range(n - 1):
            if nums[i] == -1 and nums[i + 1] != -1:
                mx = max(mx, nums[i + 1])
                mn = min(mn, nums[i + 1])
            elif nums[i] != -1 and nums[i + 1] == -1:
                mx = max(mx, nums[i])
                mn = min(mn, nums[i])

        if mn == inf:
            return lo

        hi = (mx - mn + 1) // 2
        if hi <= lo:
            return lo
        ids = []  # 与-1相邻的数的下标
        for i in range(n):
            if nums[i] == -1: continue
            if i and nums[i - 1] == -1:
                ids.append(i)
            elif i < n - 1 and nums[i + 1] == -1:
                ids.append(i)

        lo -= 1  # 保证 lo 是达不到的

        def check(val):
            x, y = mn + val, mx - val
            # 尝试用 x, y 去填充-1，检查是否能保证相邻元素差<=val
            dp = [[0] * 2 for _ in range(n)]  # 位置 i 填 x 是否可行 dp[i][0]，位置 i 填 y 是否可行 dp[i][0]
            dp[0][0] = dp[0][1] = 1
            flg = True if y - x <= val else False
            for i in range(1, n):
                if nums[i] != -1:
                    if nums[i - 1] != -1: continue
                    if dp[i - 1][0]:
                        if abs(nums[i] - x) <= val:
                            dp[i][0] = 1
                    if dp[i - 1][1]:
                        if abs(nums[i] - y) <= val:
                            dp[i][1] = 1
                else:
                    if nums[i - 1] != -1:
                        if abs(nums[i - 1] - x) <= val:
                            dp[i][0] = 1
                        if abs(nums[i - 1] - y) <= val:
                            dp[i][1] = 1
                    else:
                        if dp[i - 1][0]:
                            dp[i][0] = 1
                            dp[i][1] = flg
                        if dp[i - 1][1]:
                            dp[i][1] |= 1
                            dp[i][0] |= flg
                if dp[i][0] == dp[i][1] == 0:
                    return False
            return True


        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid
        return hi






so = Solution()
print(so.minDifference([40,-1,7,-1]))
print(so.minDifference([2,-1,4,-1,-1,6]))
print(so.minDifference([1,2]))
print(so.minDifference([1,2,-1,10,8]))




