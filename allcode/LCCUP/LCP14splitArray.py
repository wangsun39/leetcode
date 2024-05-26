# 给定一个整数数组 nums ，小李想将 nums 切割成若干个非空子数组，使得每个子数组最左边的数和最右边的数的最大公约数大于 1 。为了减少他的工作量，请求出最少可以切成多少个子数组。
# 
# 示例 1：
# 
# 输入：nums = [2,3,3,2,3,3]
# 
# 输出：2
# 
# 解释：最优切割为 [2,3,3,2] 和 [3,3] 。第一个子数组头尾数字的最大公约数为 2 ，第二个子数组头尾数字的最大公约数为 3 。
# 
# 示例 2：
# 
# 输入：nums = [2,3,5,7]
# 
# 输出：4
# 
# 解释：只有一种可行的切割：[2], [3], [5], [7]
# 
# 限制：
# 
# 1 <= nums.length <= 10^5
# 2 <= nums[i] <= 10^6

from leetcode.allcode.competition.mypackage import *

class Solution:
    def splitArray(self, nums: List[int]) -> int:
        def factors(x):
            res = []
            i = 1
            while i * i <= x:
                if x % i == 0:
                    res.append(i)
                    if i * i != x:
                        res.append(x // i)
                i += 1
            return res

        n = len(nums)
        dp = list(range(1, n + 1, 1))  # dp[i] 统计前i个数的最小切分
        # d = {}  # d[y]  # 表示所有含因子y的位置i中，具有最小切分的num[:i]的一个i
        d = {}   # d[y]  # 最近的一个含有因子y的位置
        for i, x in enumerate(nums):
            fs = factors(x)
            for y in fs:
                if y in d:
                    dp[i] = dp[d[y]]
                else:
                    if i > 0:
                        dp[i] = dp[i - 1] + 1
                    else:
                        dp[i] = 1
                d[y] = i
        return dp[-1]


so = Solution()
print(so.splitArray([2,3,3,2,3,3]))
print(so.splitArray([2,3,5,7]))



