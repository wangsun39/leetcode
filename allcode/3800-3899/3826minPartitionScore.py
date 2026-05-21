# 给你一个整数数组 nums 和一个整数 k。
#
# 你的任务是将 nums 分割成 恰好 k 个子数组，并返回所有有效分割方案中 最小可能的分数。
#
# 一个分割方案的 分数 是其所有子数组 值 的 总和。
#
# 子数组的 值 定义为 sumArr * (sumArr + 1) / 2，其中 sumArr 是该子数组元素的总和。
#
# 子数组 是数组中连续的非空元素序列。
#
#
#
# 示例 1：
#
# 输入： nums = [5,1,2,1], k = 2
#
# 输出： 25
#
# 解释：
#
# 我们必须将数组分割成 k = 2 个子数组。一种最优方案是 [5] 和 [1, 2, 1]。
# 第一个子数组的 sumArr = 5，value = 5 × 6 / 2 = 15。
# 第二个子数组的 sumArr = 1 + 2 + 1 = 4，value = 4 × 5 / 2 = 10。
# 该分割方案的分数为 15 + 10 = 25，这是可能的最小分数。
# 示例 2：
#
# 输入： nums = [1,2,3,4], k = 1
#
# 输出： 55
#
# 解释：
#
# 由于必须分割成 k = 1 个子数组，所有元素都属于同一个子数组：[1, 2, 3, 4]。
# 该子数组的 sumArr = 1 + 2 + 3 + 4 = 10，value = 10 × 11 / 2 = 55。
# 该分割方案的分数为 55，这是可能的最小分数。
# 示例 3：
#
# 输入： nums = [1,1,1], k = 3
#
# 输出： 3
#
# 解释：
#
# 我们必须将数组分割成 k = 3 个子数组。唯一的有效分割方案是 [1], [1], [1]。
# 每个子数组的 sumArr = 1，value = 1 × 2 / 2 = 1。
# 该分割方案的分数为 1 + 1 + 1 = 3，这是可能的最小分数。
#
#
# 提示：
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 104
# 1 <= k <= nums.length

from leetcode.allcode.competition.mypackage import *


class Solution:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        dp = [[0] * n for _ in range(k)]  # dp[i][j]  前j项分成i+1段的分数总和(先不除以2，最后结果除以2)
        for j in range(n):
            dp[0][j] = s[j + 1] * (s[j + 1] + 1)

        def sub(a, b):
            return [a[0] - b[0], a[1] - b[1]]

        def cross(a, b):
            return a[0] * b[1] - a[1] * b[0]

        def dot(a, b):
            return a[0] * b[0] + a[1] * b[1]

        for i in range(1, k):
            dq = deque()
            # cur = -1
            # dp[i][i] = dp[i - 1][i - 1] + nums[i] * (nums[i] + 1)

            dq.append([s[i], dp[i - 1][i - 1] + s[i] * s[i] - s[i]])
            for j in range(i, n):
                # dp[i][j] = s[j+1]^2+s[j+1] + min(dp[i-1][t]-2s[j+1]s[t+1]+s[t+1]^2-s[t+1]), 其中min是对 t在范围[i-1,j-1]上进行的
                # min中的部分进行凸包优化，转成两个向量点乘
                # v[t]=（s[t+1], dp[i-1][t]+s[t+1]^2-s[t+1])
                # p=(-2s[j],1)， p的x坐标 随着j增大，单调减小
                # dq 存放v[t] 凸包上的点，v[t]的x坐标是随着t增大，单调上升的，因此按顺序刚放入v[t]时，v[t]一定是凸包上的点，
                # 同时它也可能会顶掉前几个前面最后放入的若干个点

                p = [-2 * s[j + 1], 1]
                while len(dq) >= 2:
                    if dot(p, dq[0]) >= dot(p, dq[1]):  # 根据几何性质，当p的x坐标左移时，凸包上的点与p点乘的最小值，应该在凸包上右移
                        # 因此队列中先放入的点一旦点乘大于后续点，就可以出队了，点乘最小值发生在队列最左侧
                        dq.popleft()
                    else:
                        break
                dp[i][j] = dot(p, dq[0]) + s[j + 1] * s[j + 1] + s[j + 1]

                if j == n - 1: break
                v = [s[j + 1], dp[i - 1][j] + s[j + 1] * s[j + 1] - s[j + 1]]  # 放入在下一轮中使用的凸包中的点，它的x坐标在最右侧，下一轮中一定在凸包上
                while len(dq) >= 2:
                    x1 = sub(dq[-1], dq[-2])
                    x2 = sub(v, dq[-1])
                    if cross(x1, x2) <= 0:
                        dq.pop()
                    else:
                        break
                dq.append(v)

        # print(dp)
        return dp[-1][-1] // 2


so = Solution()
print(so.minPartitionScore(nums = [5,1,2,1], k = 2))


