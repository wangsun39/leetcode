# 给你一个下标从 0 开始的整数数组 nums 。在一步操作中，你可以：
#
# 在范围 0 <= i < nums.length 内选出一个下标 i
# 将 nums[i] 的值变为 nums[i] + 1 或 nums[i] - 1
# 返回将数组 nums 变为 非递增 或 非递减 所需的 最小 操作次数。
#
#
#
# 示例 1：
#
# 输入：nums = [3,2,4,5,0]
# 输出：4
# 解释：
# 一种可行的操作顺序，能够将 nums 变为非递增排列：
# - nums[1] 加 1 一次，使其变为 3 。
# - nums[2] 减 1 一次，使其变为 3 。
# - nums[3] 减 1 两次，使其变为 3 。
# 经过 4 次操作后，nums 变为 [3,3,3,3,0] ，按非递增顺序排列。
# 注意，也可以用 4 步操作将 nums 变为 [4,4,4,4,0] ，同样满足题目要求。
# 可以证明最少需要 4 步操作才能将数组变为非递增或非递减排列。
# 示例 2：
#
# 输入：nums = [2,2,3,4]
# 输出：0
# 解释：数组已经是按非递减顺序排列了，无需执行任何操作，返回 0 。
# 示例 3：
#
# 输入：nums = [0]
# 输出：0
# 解释：数组已经是按非递减顺序排列了，无需执行任何操作，返回 0 。
#
#
# 提示：
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
#
#
# 进阶：你可以设计并实现时间复杂度为 O(n*log(n)) 的解法吗?



from leetcode.allcode.competition.mypackage import *
class Solution:

    def convertArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        mx = max(nums)
        dp = [[0] * (mx + 1) for _ in range(n)]  # dp[i][j] 表示前i项变成末尾是j的单调增数组，最少操作次数
        for i in range(mx + 1):
            dp[0][i] = abs(nums[0] - i)
        for i in range(1, n):
            mn = inf  # 前i-1项变成末尾不超过j的最小次数
            for j in range(mx + 1):
                mn = min(mn, dp[i - 1][j])
                dp[i][j] = abs(j - nums[i]) + mn
        ans = min(dp[-1])
        dp = [[0] * (mx + 1) for _ in range(n)]  # dp[i][j] 表示前i项变成末尾是j的单调减数组，最少操作次数
        for i in range(mx + 1):
            dp[0][i] = abs(nums[0] - i)
        for i in range(1, n):
            mn = inf  # 前i-1项变成末尾不低于j的最小次数
            for j in range(mx, -1, -1):
                mn = min(mn, dp[i - 1][j])
                dp[i][j] = abs(j - nums[i]) + mn
        ans = min(ans, min(dp[-1]))
        return ans


    def convertArray2(self, nums: List[int]) -> int:
        # 优先队列的做法，还没理解
#         求变为不减数组的最小操作次数
# 对前后两个数字，例如 5 和 3，如果后面一个元素小于前面的元素，那么需要将前面的元素减小到后一个元素 (贪心)
# 遍历数组，维护看过的最大值，如果之前的最大值大于当前元素，那么就把这个最大值变为当前元素
# 时间复杂度 O(nlogn)

#         通过一个例子来解释这个基于堆的算法：1 5 10 4 2 2 2 2
# 假设当前维护的是非降序列，前三个数直接插入，不需要任何修改
# 插入 4 的时候，可以修改为 1 5 5 5，或 1 5 6 6，或... 1 5 10 10，修改次数均为 6
# 但我们也可以把修改后的序列视作 1 5 4 4，虽然序列不为非降序列，但修改的次数仍然为 6
# 接下来插入 2，基于 1 5 5 5 的话，修改后的序列就是 1 5 5 5 5，总的修改次数为 9
# 但我们也可以把修改后的序列视作 1 2 4 4 2，总的修改次数仍然为 9
# 接下来插入 2，如果基于 1 5 5 5 5 变成 1 5 5 5 5 5，会得到错误的修改次数 12
# 但是实际上有更优的修改 1 4 4 4 4 4，总的修改次数为 11
# 同上，把这个序列视作 1 2 2 4 2 2，总的修改次数仍然为 11
# https://leetcode.cn/link/?target=https%3A%2F%2Fcodeforces.com%2Fblog%2Fentry%2F47821

        def helper(nums: List[int]) -> int:
            """变为不减数组的最小操作次数"""
            res, pq = 0, []  # 大根堆
            for num in nums:
                if not pq:
                    heappush(pq, -num)
                else:
                    preMax = -pq[0]
                    if preMax > num:
                        res += preMax - num
                        heappushpop(pq, -num)
                    heappush(pq, -num)
            return res

        return min(helper(nums), helper(nums[::-1]))


so = Solution()
print(so.convertArray([0,0,0,0]))
print(so.convertArray([3,2,4,5,0]))
print(so.convertArray([2,2,3,4]))
print(so.convertArray([0]))


