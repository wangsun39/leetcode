# 给你一个整数数组 nums 和一个整数 k 。区间 [left, right]（left <= right）的 异或结果 是对下标位于 left 和 right（包括 left 和 right ）之间所有元素进行 XOR 运算的结果：nums[left] XOR nums[left+1] XOR ... XOR nums[right] 。
# 
# 返回数组中 要更改的最小元素数 ，以使所有长度为 k 的区间异或结果等于零。
# 
#  
# 
# 示例 1：
# 
# 输入：nums = [1,2,0,3,0], k = 1
# 输出：3
# 解释：将数组 [1,2,0,3,0] 修改为 [0,0,0,0,0]
# 示例 2：
# 
# 输入：nums = [3,4,5,2,1,7,3,4,7], k = 3
# 输出：3
# 解释：将数组 [3,4,5,2,1,7,3,4,7] 修改为 [3,4,7,3,4,7,3,4,7]
# 示例 3：
# 
# 输入：nums = [1,2,4,1,2,5,1,2,6], k = 3
# 输出：3
# 解释：将数组[1,2,4,1,2,5,1,2,6] 修改为 [1,2,3,1,2,3,1,2,3]
#  
# 
# 提示：
# 
# 1 <= k <= nums.length <= 2000
# 0 <= nums[i] < 210

from leetcode.allcode.competition.mypackage import *


min = lambda a, b: b if b < a else a

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        M = 1024  # 最大元素
        change = [defaultdict(int) for _ in range(k)]  # 第i个分组都变成j的最小改变次数，在分组中没出现的不统计
        size = [0] * k
        for i in range(k):
            counter = defaultdict(int)
            for j in range(i, n, k):
                counter[nums[j]] += 1
                size[i] += 1
            for u, v in counter.items():
                change[i][u] = size[i] - v
        dp = [[0] * M for _ in range(k)]  # 前i个分组的异或变成j，总的最小改变次数
        pre_mn = size[0]  # 前一组最小的变换次数
        for j in range(M):
            dp[0][j] = change[0][j] if j in change[0] else size[0]
            pre_mn = min(pre_mn, dp[0][j])
        for i in range(1, k):
            cur_mn = size[i] + pre_mn
            for j in range(M):
                dp[i][j] = size[i] + pre_mn  # 这步优化比较关键，本组内没有的数字，变换次数就为size[i]
                for u, v in change[i].items():
                    dp[i][j] = min(dp[i - 1][j ^ u] + v, dp[i][j])
                cur_mn = min(cur_mn, dp[i][j])
            pre_mn = cur_mn
        return dp[-1][0]


so = Solution()

print(so.minChanges(nums = [26,19,19,28,13,14,6], k = 3))  # 5
print(so.minChanges(nums = [1,2,0,3,0], k = 1))  # 3




