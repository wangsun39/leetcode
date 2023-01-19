# 如果一个密码满足以下所有条件，我们称它是一个 强 密码：
#
# 它有至少 8 个字符。
# 至少包含 一个小写英文 字母。
# 至少包含 一个大写英文 字母。
# 至少包含 一个数字 。
# 至少包含 一个特殊字符 。特殊字符为："!@#$%^&*()-+" 中的一个。
# 它 不 包含 2 个连续相同的字符（比方说 "aab" 不符合该条件，但是 "aba" 符合该条件）。
# 给你一个字符串 password ，如果它是一个 强 密码，返回 true，否则返回 false 。
#
#
#
# 示例 1：
#
# 输入：password = "IloveLe3tcode!"
# 输出：true
# 解释：密码满足所有的要求，所以我们返回 true 。
# 示例 2：
#
# 输入：password = "Me+You--IsMyDream"
# 输出：false
# 解释：密码不包含数字，且包含 2 个连续相同的字符。所以我们返回 false 。
# 示例 3：
#
# 输入：password = "1aB!"
# 输出：false
# 解释：密码不符合长度要求。所以我们返回 false 。
#
#
# 提示：
#
# 1 <= password.length <= 100
# password 包含字母，数字和 "!@#$%^&*()-+" 这些特殊字符。


from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)


import bisect
# bisect_right：
# 若序列a中存在与x相同的元素，则返回x相等元素右侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x左侧距离最近元素插入点的索引位置
# pos = bisect.bisect_right(left, tail)
# bisect_left：
# 若序列a中存在与x相同的元素，则返回x相等元素左侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x右侧距离最近元素插入点的索引位置

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache
from typing import List
# @lru_cache(None)

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8: return False
        flg1 = flg2 = flg3 = flg4 = False
        for i, x in enumerate(password):
            if x.islower():
                flg1 = True
            elif x.isupper():
                flg2 = True
            elif x.isdigit(): flg3 = True
            elif x in '!@#$%^&*()-+': flg4 = True
            if i > 0 and x == password[i - 1]:
                return False
        return flg1 and flg2 and flg3 and flg4




so = Solution()
print(so.strongPasswordCheckerII("IloveLe3tcode!"))
print(so.strongPasswordCheckerII("Me+You--IsMyDream"))




