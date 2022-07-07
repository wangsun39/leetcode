# 给你一个字符串 s ，每 两个 连续竖线 '|' 为 一对 。换言之，第一个和第二个 '|' 为一对，第三个和第四个 '|' 为一对，以此类推。
#
# 请你返回 不在 竖线对之间，s 中 '*' 的数目。
#
# 注意，每个竖线 '|' 都会 恰好 属于一个对。
#
#  
#
# 示例 1：
#
# 输入：s = "l|*e*et|c**o|*de|"
# 输出：2
# 解释：不在竖线对之间的字符加粗加斜体后，得到字符串："l|*e*et|c**o|*de|" 。
# 第一和第二条竖线 '|' 之间的字符不计入答案。
# 同时，第三条和第四条竖线 '|' 之间的字符也不计入答案。
# 不在竖线对之间总共有 2 个星号，所以我们返回 2 。
# 示例 2：
#
# 输入：s = "iamprogrammer"
# 输出：0
# 解释：在这个例子中，s 中没有星号。所以返回 0 。
# 示例 3：
#
# 输入：s = "yo|uar|e**|b|e***au|tifu|l"
# 输出：5
# 解释：需要考虑的字符加粗加斜体后："yo|uar|e**|b|e***au|tifu|l" 。不在竖线对之间总共有 5 个星号。所以我们返回 5 。
#  
#
# 提示：
#
# 1 <= s.length <= 1000
# s 只包含小写英文字母，竖线 '|' 和星号 '*' 。
# s 包含 偶数 个竖线 '|' 。

from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
#import random
# random.uniform(a, b)，用于生成一个指定范围内的随机浮点数，闭区间
# randint和randrange的区别：
# randint 产生的随机数区间是包含左右极限的，也就是说左右都是闭区间的[1, n]，能取到1和n。
# 而 randrange 产生的随机数区间只包含左极限，也就是左闭右开的[1, n)，1能取到，而n取不到。

# 浮点数： price = "{:.02f}".format(price)
# newword = float(word[1:]) * (100 - discount) / 100
# newword = "%.2f" % newword

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

# bit位 函数：
# n.bit_length()
# value = int(s, 2)

class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        ans = 0
        for e in s:
            if e == '*' and count % 2 == 0:
                ans += 1
            if e == '|':
                count += 1
        return ans


so = Solution()
print(so.countAsterisks("l|*e*et|c**o|*de|*"))
print(so.countAsterisks("yo|uar|e**|b|e***au|tifu|l"))
print(so.countAsterisks("abc"))




