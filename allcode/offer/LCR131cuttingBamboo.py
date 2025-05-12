# 现需要将一根长为正整数 bamboo_len 的竹子砍为若干段，每段长度均为正整数。请返回每段竹子长度的最大乘积是多少。
#
#
#
# 示例 1：
#
# 输入: bamboo_len = 12
# 输出: 81
# 提示：
# 2 <= bamboo_len <= 58
# 注意：本题与主站 343 题相同： https://leetcode-cn.com/problems/integer-break/

from leetcode.allcode.competition.mypackage import *

class Solution:
    def cuttingBamboo(self, bamboo_len: int) -> int:
        if bamboo_len == 3: return 2
        if bamboo_len <= 4: return bamboo_len
        m = bamboo_len // 3
        if bamboo_len % 3 == 0:
            return 3 ** m
        if bamboo_len % 3 == 2:
            return (3 ** m) * 2
        return (3 ** (m - 1)) * 4

so = Solution()




