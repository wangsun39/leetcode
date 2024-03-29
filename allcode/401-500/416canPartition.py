class Solution:
    def canPartition(self, nums):
        M = sum(nums)
        if M % 2 == 1:
            return False
        half_M = M // 2
        total_unit = len(nums)
        # 背包问题：m的行表示包的个数，列表示包的总体积上限
        m = [[0] * (half_M + 1) for _ in range(total_unit+1)]
        for j in range(1, half_M + 1):
            for i in range(1, total_unit+1):
                if j >= nums[i-1]:
                    m[i][j] = max(m[i-1][j], m[i-1][j-nums[i-1]]+nums[i-1])
                else:
                    m[i][j] =m[i-1][j]
        return m[total_unit][half_M] == half_M

    def canPartition1(self, nums: List[int]) -> bool:
        # 2023/5/23  记忆化搜索
        n = len(nums)
        @cache
        def dfs(idx, s): # 前 i 个数的子集，能否构成和s
            if idx == 0: return s == 0 or s == nums[0]
            return dfs(idx - 1, s) or dfs(idx - 1, s - nums[idx])
        s = sum(nums)
        if s & 1: return False
        return dfs(n - 1, s // 2)

    def canPartition(self, nums: List[int]) -> bool:
        # 2023/9/12 DP
        s = sum(nums)
        n = len(nums)
        if s & 1: return False
        dp = [[0] * (s // 2) for _ in range(n)]  # dp[i][j] 表示前i项，是否会出现和为j的子集
        if nums[0] == s // 2:
            return True
        elif nums[0] < s // 2:
            dp[0][nums[0]] = 1
        for i, x in enumerate(nums[1:], 1):
            if x == s // 2: return True
            if x > s // 2: return False
            dp[i][x] = 1
            for j in range(s // 2):
                if dp[i - 1][j]:
                    dp[i][j] = 1
                    if j + x == s // 2:
                        return True
                    elif j + x < s // 2:
                        dp[i][j + x] = 1
        return False



so = Solution()
print(so.canPartition([1, 5, 11, 5]))
print(so.canPartition([91,29,92,14,53,27,96,97,58,76,56,51,68,18,37,98,30,37,25,65,95,22,34,25,29,37,54,34,43,18,65,31,21,91,9,57,13,72,31,26,36,77,85,70,5,72,93,39,46,50,22,16,6,67,17,41,42,10,56,66,69,53,79,46,14,34,80,31,86,78,35,64,75,88,58,26,56,91,84,38,44,19,49,8,4,78,11,13,10,56,72,97,25,62,97,80,20,63,5,27]))
#print(so.diffWaysToCompute("2*3-4*5"))

