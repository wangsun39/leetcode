# 编写一个方法，计算从 0 到 n (含 n) 中数字 2 出现的次数。
#
# 示例:
#
# 输入: 25
# 输出: 9
# 解释: (2, 12, 20, 21, 22, 23, 24, 25)(注意 22 应该算作两次)
# 提示：
#
# n <= 10^9


from typing import List
from collections import defaultdict
from functools import lru_cache

class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        s = str(n)
        @lru_cache(None)
        def helper(i: int, num2: int, is_limit: bool) -> int:
            if i == len(s):
                return num2
            ans = 0
            upper = int(s[i]) if is_limit else 9  # 判断当前位是否受约束
            for j in range(upper + 1):
                ans += helper(i + 1, num2 + (j == 2), is_limit and j == upper)
            return ans
        return helper(0, 0, True)





so = Solution()
print(so.numberOf2sInRange(25))




