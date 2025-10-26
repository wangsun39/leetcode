# 给你一个正整数n。
#
# 返回一个整数，该整数是将 n 的十进制表示中所有的零都移除后得到的结果。
#
#
#
# 示例 1：
#
# 输入： n = 1020030
#
# 输出： 123
#
# 解释：
#
# 从 1020030 中移除所有的零后，得到 123。
#
# 示例 2：
#
# 输入： n = 1
#
# 输出： 1
#
# 解释：
#
# 1 的十进制表示中没有零，因此结果为 1。
#
#
#
# 提示：
#
# 1 <= n <= 1015

from leetcode.allcode.competition.mypackage import *

class Solution:
    def removeZeros(self, n: int) -> int:
        s = str(n)
        res = []
        for x in s:
            if x != '0':
                res.append(x)
        ans = ''.join(res)
        return int(ans)
    'abc'.st


so = Solution()




