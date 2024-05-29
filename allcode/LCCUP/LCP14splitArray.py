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


# 预处理计算所有数的最小质因子
max_num = 1000000
min_factor = [1] * (max_num + 1)  # 记录每个数x的最小质因子 min_factor[x]
p = 2
min_factor[2] = 2
# O(M loglog M)
while p <= max_num:
    i = p
    while i * p <= max_num:
        if min_factor[i * p] == 1:
            min_factor[i * p] = p
        i += 1

    p += 1
    while p <= max_num:
        if min_factor[p] == 1:
            min_factor[p] = p
            break
        p += 1



class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = list(range(1, n + 1, 1))  # dp[i] 统计前i个数的最小切分
        d = {}   # d[y]  # 含有因子y的位置的前一个位置的最小切分
        for i, x in enumerate(nums):
            if i > 0:
                dp[i] = dp[i - 1] + 1  # x不与前面的数在一个切分
            # 下面就是x与前面的某个数具有相同因子，就要遍历所有x的质因子，将其放入一个切分之中
            while min_factor[x] > 1:
                y = min_factor[x]
                if y in d:
                    dp[i] = min(dp[i], d[y] + 1)  # x与前面某个数具有公因子y，且他们在一个切分中
                    d[y] = min(d[y], dp[i - 1])
                else:
                    d[y] = dp[i - 1] if i else 0
                while x % y == 0:
                    x //= y

        return dp[-1]


so = Solution()
print(so.splitArray([2,3,5,7]))  # 4
print(so.splitArray([2,3,3,2,3,3]))  # 2



