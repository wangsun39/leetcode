# 给你一个字符串 s 和一个字符 letter ，返回在 s 中等于 letter 字符所占的 百分比 ，向下取整到最接近的百分比。
#
#  
#
# 示例 1：
#
# 输入：s = "foobar", letter = "o"
# 输出：33
# 解释：
# 等于字母 'o' 的字符在 s 中占到的百分比是 2 / 6 * 100% = 33% ，向下取整，所以返回 33 。
# 示例 2：
#
# 输入：s = "jjjj", letter = "k"
# 输出：0
# 解释：
# 等于字母 'k' 的字符在 s 中占到的百分比是 0% ，所以返回 0 。
#  
#
# 提示：
#
# 1 <= s.length <= 100
# s 由小写英文字母组成
# letter 是一个小写英文字母

# Map = [['U' for _ in range(n)] for _ in range(m)]

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

from functools import lru_cache
from typing import List
# @lru_cache(None)

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = len(s)
        counter = Counter(list(s))
        print(counter)
        return counter[letter] * 100 // n


so = Solution()
print(so.percentageLetter("foobar", letter = "o"))
print(so.percentageLetter(s = "jjjj", letter = "k"))




