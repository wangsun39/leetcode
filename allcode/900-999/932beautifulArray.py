# 如果长度为 n 的数组 nums 满足下述条件，则认为该数组是一个 漂亮数组 ：
# 
# nums 是由范围 [1, n] 的整数组成的一个排列。
# 对于每个 0 <= i < j < n ，均不存在下标 k（i < k < j）使得 2 * nums[k] == nums[i] + nums[j] 。
# 给你整数 n ，返回长度为 n 的任一 漂亮数组 。本题保证对于给定的 n 至少存在一个有效答案。
# 
#  
# 
# 示例 1 ：
# 
# 输入：n = 4
# 输出：[2,1,4,3]
# 示例 2 ：
# 
# 输入：n = 5
# 输出：[3,1,2,5,4]
#  
# 
# 提示：r
# 
# 1 <= n <= 1000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def beautifulArray(self, n: int) -> List[int]:

        @cache
        def dfs(n):
            if n == 1:
                return [1]
            if n == 2:
                return [1, 2]
            if n & 1:
                odds = dfs((n + 1) // 2)
                even = dfs(n // 2)
                return [x * 2 - 1 for x in odds] + [x * 2 for x in even]
            else:
                even = dfs(n // 2)
                return [x * 2 - 1 for x in even] + [x * 2 for x in even]
        return dfs(n)


so = Solution()
print(so.beautifulArray(4))
