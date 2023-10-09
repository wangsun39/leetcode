# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
#
#  
#
# 示例 1:
#
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 示例 2:
#
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。



from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        dp1 = [0] * N   # 记录以nums[i]结尾的字串大于等于0的最大乘积
        dp2 = [0] * N   # 记录以nums[i]结尾的字串小于等于0的最小乘积
        dp1[0], dp2[0] = nums[0], nums[0]
        for i in range(1, N):
            if nums[i] > 0:
                dp1[i], dp2[i] = max(nums[i], dp1[i-1] * nums[i]), dp2[i-1] * nums[i]
            else:
                dp1[i], dp2[i] = dp2[i - 1] * nums[i], min(nums[i], dp1[i - 1] * nums[i])
        # print(dp1, dp2)

        return max(dp1)


so = Solution()
print(so.maxProduct([1,2,-1,-2,2,1,-2,1,4,-5,4]))
print(so.maxProduct([-2,3,-4]))
print(so.maxProduct([-2]))
print(so.maxProduct([2,3,-2,4]))
print(so.maxProduct([-2,0,-1]))

