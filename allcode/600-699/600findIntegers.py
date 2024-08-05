# 给定一个正整数 n ，返回范围在 [0, n] 都非负整数中，其二进制表示不包含 连续的 1 的个数。
#
#  
#
# 示例 1:
#
# 输入: n = 5
# 输出: 5
# 解释:
# 下面是带有相应二进制表示的非负整数<= 5：
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# 其中，只有整数3违反规则（有两个连续的1），其他5个满足规则。
# 示例 2:
#
# 输入: n = 1
# 输出: 2
# 示例 3:
#
# 输入: n = 2
# 输出: 3
#  
#
# 提示:
#
# 1 <= n <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findIntegers1(self, n: int) -> int:
        s = bin(n)[2:]
        @lru_cache(None)
        def helper(i: int, pre, is_limit: bool) -> int:
            if i == len(s):
                return 1
            ans = 0
            upper = int(s[i]) if is_limit else 1  # 判断当前位是否受约束
            for j in range(upper + 1):
                if j == 1 and i > 0 and pre == 1:
                    continue
                ans += helper(i + 1, j, is_limit and j == upper)
            return ans
        return helper(0, 0, True)

    def findIntegers(self, n: int) -> int:
        # 2024/8/5 重写一次
        @cache
        def helper(i: int, pre: int, is_limit: bool) -> int:
            if i == len(s):
                return 1
            ans = 0
            upper = int(s[i]) if is_limit else 1  # 判断当前位是否受约束
            if pre == 1: upper = min(upper, 0)
            lower = 0
            for j in range(lower, upper + 1):
                ans += helper(i + 1, j, is_limit and j == int(s[i]))
            return ans

        s = bin(n)[2:]

        return helper(0, 0, True)




so = Solution()

print('ret = ', so.findIntegers(6)) # 5
print('ret = ', so.findIntegers(1)) # 2
print('ret = ', so.findIntegers(5)) # 5
print('ret = ', so.findIntegers(2)) # 3


