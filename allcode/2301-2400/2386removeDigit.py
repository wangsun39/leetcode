# 给你一个整数数组 nums 和一个 正 整数 k 。你可以选择数组的任一 子序列 并且对其全部元素求和。
#
# 数组的 第 k 大和 定义为：可以获得的第 k 个 最大 子序列和（子序列和允许出现重复）
#
# 返回数组的 第 k 大和 。
#
# 子序列是一个可以由其他数组删除某些或不删除元素派生而来的数组，且派生过程不改变剩余元素的顺序。
#
# 注意：空子序列的和视作 0 。
#
#
#
# 示例 1：
#
# 输入：nums = [2,4,-2], k = 5
# 输出：2
# 解释：所有可能获得的子序列和列出如下，按递减顺序排列：
# - 6、4、4、2、2、0、0、-2
# 数组的第 5 大和是 2 。
# 示例 2：
#
# 输入：nums = [1,-2,3,4,-10,12], k = 16
# 输出：10
# 解释：数组的第 16 大和是 10 。
#
#
# 提示：
#
# n == nums.length
# 1 <= n <= 105
# -109 <= nums[i] <= 109
# 1 <= k <= min(2000, 2n)


from leetcode.allcode.competition.mypackage import *

class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]   # 改成求第k小，最后求相反数
        s1 = sum(x for x in nums if x < 0)  # 所有负数之和就是最小值
        nums = [x * (-1) if x < 0 else x for x in nums]  # 将负数变成正数
        nums.sort()

        n = len(nums)
        hp = [[s1, -1]]   # [子序列和，子序列最后一项下标]
        v = 0
        for _ in range(k):
            v, idx = heappop(hp)
            if idx + 1 < n:
                if v + nums[idx + 1] == 0:  # 追加一个元素
                    heappush(hp, [v + nums[idx + 1], idx + 1])
                else:
                    heappush(hp, [v + nums[idx + 1], idx + 1])
                if idx == -1: continue
                if v - nums[idx] + nums[idx + 1] == 0:  # 替换最后一个元素
                    heappush(hp, [v - nums[idx] + nums[idx + 1], idx + 1])
                else:
                    heappush(hp, [v - nums[idx] + nums[idx + 1], idx + 1])
            # print(v)
        return -v




so = Solution()
print(so.kSum(nums = [-530219056,353285209,493533664], k = 6))
print(so.kSum(nums = [2,4,-2], k = 5))
print(so.kSum(nums = [1,-2,3,4,-10,12], k = 16))




