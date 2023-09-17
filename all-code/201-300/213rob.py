class Solution:
    def rob1(self, nums) -> int:
        num = len(nums)
        if 1 == num:
            return nums[0]
        elif 2 == num:
            return max(nums[0], nums[1])
        elif 0 == num:
            return 0
        F1 = self.getF1Value(num, nums)
        F2 = self.getF2Value(num, nums)
        return max(F1[(num-1)-1], F2[(num-1)-2]+nums[-1])
    def getF1Value(self, num, nums):
        # 房屋不绕圈时的解，动态规划
        F = [0] * num
        F[0], F[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, num):
            F[i] = max(F[i-1], F[i-2] + nums[i])
        return F
    def getF2Value(self, num, nums):
        # 房屋不绕圈，且不偷窃第0个房间时的解，动态规划
        F = [0] * num
        F[1], F[2] = nums[1], max(nums[1], nums[2])
        for i in range(3, num):
            F[i] = max(F[i-1], F[i-2] + nums[i])
        return F

    def rob(self, nums: List[int]) -> int:
        # 2023/9/17  调用213题的函数
        if len(nums) == 1: return nums[0]
        def rob1(nums):
            dp = [0, 0]  # 偷i-1的最大金额，不偷i-1的最大金额
            for x in nums:
                u = dp[1] + x
                v = max(dp)
                dp = [u, v]
            return max(dp)
        return max(rob1(nums[1:]), rob1(nums[:-1]))

so = Solution()
#print(so.findKthLargest([3,2,1,5,6,4], 2))
#print(so.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
#print(so.findKthLargest([7,6,5,4,3,2,1], 5))
print(so.findKthLargest([1,2,3,4,5,6], 1))

