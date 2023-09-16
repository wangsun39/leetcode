class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob1(self, nums) -> int:
        num = len(nums)
        if 1 == num:
            return nums[0]
        elif 2 == num:
            return max(nums[0], nums[1])
        elif 0 == num:
            return 0
        # 动态规划,F[i]表示前i的房屋的产出最大值
        F = [0] * num
        F[0], F[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, num):
            F[i] = max(F[i - 1], F[i - 2] + nums[i])
        return F[num-1]

    def rob(self, nums: List[int]) -> int:
        # 2023/9/16
        dp1 = [0, 0]  # 偷i-2的最大金额，不偷i-2的最大金额
        dp2 = [0, 0]  # 偷i-1的最大金额，不偷i-1的最大金额
        for i, x in enumerate(nums):
            u = max(max(dp1), dp2[1]) + x
            v = max(dp2)
            dp1, dp2 = dp2, [u, v]
        return max(dp2)

so = Solution()

print(so.rob([1,2,3,1]))
print(so.rob([2,7,9,3,1]))
