class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, nums) -> int:
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

so = Solution()

print(so.rob([1,2,3,1]))
print(so.rob([2,7,9,3,1]))
