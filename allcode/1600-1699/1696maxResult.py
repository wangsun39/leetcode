# 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。
#
# 一开始你在下标 0 处。每一步，你最多可以往前跳 k 步，但你不能跳出数组的边界。也就是说，你可以从下标 i 跳到 [i + 1， min(n - 1, i + k)] 包含 两个端点的任意位置。
#
# 你的目标是到达数组最后一个位置（下标为 n - 1 ），你的 得分 为经过的所有数字之和。
#
# 请你返回你能得到的 最大得分 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,-1,-2,4,-7,3], k = 2
# 输出：7
# 解释：你可以选择子序列 [1,-1,4,3] （上面加粗的数字），和为 7 。
# 示例 2：
#
# 输入：nums = [10,-5,-2,4,0,3], k = 3
# 输出：17
# 解释：你可以选择子序列 [10,4,3] （上面加粗数字），和为 17 。
# 示例 3：
#
# 输入：nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
# 输出：0
#
#
# 提示：
#
#  1 <= nums.length, k <= 105
# -104 <= nums[i] <= 104

from leetcode.allcode.competition.mypackage import *

class Solution:

    def maxResult1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        sl = SortedList([nums[n - 1]])
        dp[n - 1] = nums[n - 1]  # 从 i 到 n - 1的最大得分
        for i in range(n - 2, -1, -1):
            if len(sl) > k:
                sl.remove(dp[i + k + 1])
            dp[i] = nums[i] + sl[-1]
            sl.add(dp[i])
        return dp[0]


    def maxResult2(self, nums: List[int], k: int) -> int:
        # 优先队列
        n = len(nums)
        hp = [[-nums[0], 0]]  # 堆
        dp = nums[0]
        for i in range(1, n):
            while len(hp) > 0 and i - hp[0][1] > k:
                heappop(hp)
            x, j = hp[0]
            dp = -x + nums[i]   # 到达 nums[i] 的最大得分
            heappush(hp, [-dp, i])
        return dp

    def maxResult(self, nums: List[int], k: int) -> int:
        # 单调队列
        n = len(nums)
        q = deque([[nums[0], 0]])  # 单调队列
        dp = nums[0]
        for i in range(1, n):
            while i - q[0][1] > k:
                q.popleft()
            x, j = q[0]
            dp = x + nums[i]   # 到达 nums[i] 的最大得分
            while q and q[-1][0] < dp:
                q.pop()
            q.append([dp, i])
        return dp

so = Solution()
print(so.maxResult(nums = [100,-1,-100,-1,100], k = 2))
print(so.maxResult(nums = [10,-5,-2,4,0,3], k = 3))
print(so.maxResult(nums = [1,-1,-2,4,-7,3], k = 2))
print(so.maxResult(nums = [1,-5,-20,4,-1,3,-6,-3], k = 2))




