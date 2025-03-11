# 给定正整数n，返回在[1, n]范围内具有 至少 1 位 重复数字的正整数的个数。
#
# 
#
# 示例 1：
#
# 输入：n = 20
# 输出：1
# 解释：具有至少 1 位重复数字的正数（<= 20）只有 11 。
# 示例 2：
#
# 输入：n = 100
# 输出：10
# 解释：具有至少 1 位重复数字的正数（<= 100）有 11，22，33，44，55，66，77，88，99 和 100 。
# 示例 3：
#
# 输入：n = 1000
# 输出：262
# 
#
# 提示：
#
# 1 <= n <= 109


from leetcode.allcode.competition.mypackage import *

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)
        @lru_cache(None)
        def helper(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                return 1 if is_num else 0
            ans = 0
            if not is_num:
                ans = helper(i + 1, mask, False, False)
            upper = int(s[i]) if is_limit else 9  # 判断当前位是否受约束
            lower = 0 if is_num else 1
            for j in range(lower, upper + 1):
                if (1 << j) & mask == 0:
                    ans += helper(i + 1, mask | (1 << j), is_limit and j == upper, True)
            return ans
        return n - helper(0, 0, True, False)



obj = Solution()
print(obj.numDupDigitsAtMostN(20))
print(obj.numDupDigitsAtMostN(100))
print(obj.numDupDigitsAtMostN(1000))

