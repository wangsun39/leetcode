# 给你一个整数数组 nums 和两个整数 x 和 k。你可以执行以下操作任意次（包括零次）：
#
# 将 nums 中的任意一个元素加 1 或减 1。
# 返回为了使 nums 中 至少 包含 k 个长度 恰好 为 x 的不重叠子数组（每个子数组中的所有元素都相等）所需要的 最少 操作数。
#
# 子数组 是数组中连续、非空的一段元素。
#
#
#
# 示例 1：
#
# 输入： nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2
#
# 输出： 8
#
# 解释：
#
# 进行 3 次操作，将 nums[1] 加 3；进行 2 次操作，将 nums[3] 减 2。得到的数组为 [5, 1, 1, 1, 7, 3, 6, 4, -1]。
# 进行 1 次操作，将 nums[5] 加 1；进行 2 次操作，将 nums[6] 减 2。得到的数组为 [5, 1, 1, 1, 7, 4, 4, 4, -1]。
# 现在，子数组 [1, 1, 1]（下标 1 到 3）和 [4, 4, 4]（下标 5 到 7）中的所有元素都相等。总共进行了 8 次操作，因此输出为 8。
# 示例 2：
#
# 输入： nums = [9,-2,-2,-2,1,5], x = 2, k = 2
#
# 输出： 3
#
# 解释：
#
# 进行 3 次操作，将 nums[4] 减 3。得到的数组为 [9, -2, -2, -2, -2, 5]。
# 现在，子数组 [-2, -2]（下标 1 到 2）和 [-2, -2]（下标 3 到 4）中的所有元素都相等。总共进行了 3 次操作，因此输出为 3。
#
#
# 提示：
#
# 2 <= nums.length <= 105
# -106 <= nums[i] <= 106
# 2 <= x <= nums.length
# 1 <= k <= 15
# 2 <= k * x <= nums.length

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        part = sorted(nums[:x])
        # 对顶堆
        less = [-y for y in part[:(x + 1)//2]]
        more = part[(x + 1)//2:]
        n1, n2 = len(less), len(more)
        heapify(less)
        heapify(more)
        mid = [-less[0]]  # 滑窗中位数
        oper = [sum(abs(y - (-less[0])) for y in nums[:x])]  # 滑窗中需要操作的数量
        de = Counter()  # 预删除计数
        for i, y in enumerate(nums[x:], x):
            pre = nums[i - x]
            de[pre] += 1
            delta = -abs(mid[i - x] - pre)  # 操作数量的差值，先减掉 pre 与 之前中位数的差
            if pre <= -less[0]:
                while less and de[-less[0]]:
                    de[-less[0]] -= 1
                    heappop(less)
                if len(more) == 0 or y <= more[0]:
                    # 删掉的和插入的都在less中
                    heappush(less, -y)
                    delta += (mid[-1] - (-less[0])) * n2  # -less[0] 是新的中位数，mid[-1]是上个窗口的中位数
                    delta += (-less[0] - mid[-1]) * (n1 - 1)
                else:
                    # 删掉的在less中 插入的在more中，需要从more挪一个到less中
                    heappush(less, -heappop(more))
                    heappush(more, y)
                    while de[more[0]]:
                        de[more[0]] -= 1
                        heappop(more)
                    delta -= (-less[0] - mid[-1]) * n2
                    delta += (-less[0] - mid[-1]) * (n1 - 1)
            else:
                while more and de[more[0]]:
                    de[more[0]] -= 1
                    heappop(more)
                if y >= -less[0]:
                    # 删掉的和插入的都在more中
                    heappush(more, y)
                else:
                    # 删掉的在more中 插入的在less中，需要从less挪一个到more中
                    heappush(more, -heappop(less))
                    heappush(less, -y)
                    while less and de[-less[0]]:
                        de[-less[0]] -= 1
                        heappop(less)
                    delta += (mid[-1] - (-less[0])) * n2
                    delta -= (mid[-1] - (-less[0])) * (n1 - 1)
            mid.append(-less[0])
            delta += abs(y - mid[-1])  # 最后加上 y 与 当前中位数的差
            oper.append(oper[-1] + delta)
        print(mid)
        print(oper)
        n = len(mid)
        # 剩下就是在oper中选k个值，使其总和最小，但要保证相邻的两个下标至少相差x
        dp = [[inf] * (k + 1) for _ in range(n)]  # dp[i][j]  前i个数中，选j个数的最小和
        for i in range(n):
            dp[i][0] = 0
            if i > 0:
                dp[i][1] = min(dp[i - 1][1], oper[i])
            else:
                dp[i][1] = oper[i]
            for j in range(2, k + 1):
                if i + x < j * x: break
                if i >= x:
                    dp[i][j] = min(dp[i - 1][j], dp[i - x][j - 1] + oper[i])
                else:
                    dp[i][j] = dp[i - 1][j]
        print(dp)
        return dp[-1][-1]






so = Solution()
print(so.minOperations(nums = [-7,7,14,19,1,-8,-2,-10,-14], x = 5, k = 1))
print(so.minOperations(nums = [9,-2,-2,-2,1,5], x = 2, k = 2))
print(so.minOperations(nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2))




