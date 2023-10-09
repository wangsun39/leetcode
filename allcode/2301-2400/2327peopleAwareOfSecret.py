# 在第 1 天，有一个人发现了一个秘密。
#
# 给你一个整数 delay ，表示每个人会在发现秘密后的 delay 天之后，每天 给一个新的人 分享 秘密。同时给你一个整数 forget ，表示每个人在发现秘密 forget 天之后会 忘记 这个秘密。一个人 不能 在忘记秘密那一天及之后的日子里分享秘密。
#
# 给你一个整数 n ，请你返回在第 n 天结束时，知道秘密的人数。由于答案可能会很大，请你将结果对 109 + 7 取余 后返回。
#
#  
#
# 示例 1：
#
# 输入：n = 6, delay = 2, forget = 4
# 输出：5
# 解释：
# 第 1 天：假设第一个人叫 A 。（一个人知道秘密）
# 第 2 天：A 是唯一一个知道秘密的人。（一个人知道秘密）
# 第 3 天：A 把秘密分享给 B 。（两个人知道秘密）
# 第 4 天：A 把秘密分享给一个新的人 C 。（三个人知道秘密）
# 第 5 天：A 忘记了秘密，B 把秘密分享给一个新的人 D 。（三个人知道秘密）
# 第 6 天：B 把秘密分享给 E，C 把秘密分享给 F 。（五个人知道秘密）
# 示例 2：
#
# 输入：n = 4, delay = 1, forget = 3
# 输出：6
# 解释：
# 第 1 天：第一个知道秘密的人为 A 。（一个人知道秘密）
# 第 2 天：A 把秘密分享给 B 。（两个人知道秘密）
# 第 3 天：A 和 B 把秘密分享给 2 个新的人 C 和 D 。（四个人知道秘密）
# 第 4 天：A 忘记了秘密，B、C、D 分别分享给 3 个新的人。（六个人知道秘密）
#  
#
# 提示：
#
# 2 <= n <= 1000
# 1 <= delay < forget <= n

from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
import random
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
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        N = int(1e9 + 7)
        f = [0] * n
        g = [0] * n
        for i in range(delay):
            f[i] = 1
        g[0] = 1
        for i in range(delay, forget):
            g[i] = sum(g[:i - delay + 1]) % N
            f[i] = (g[i] + f[i - 1]) % N
        for i in range(forget, n):
            s = 0
            for j in range(i - forget + 1, i - delay + 1):
                s += g[j]
                s %= N
            g[i] = s
            f[i] = (g[i] - g[i - forget] + f[i - 1]) % N
        print(g)
        print(f)
        return f[-1]


so = Solution()
print(so.peopleAwareOfSecret(n = 7, delay = 3, forget = 5))
print(so.peopleAwareOfSecret(n = 6, delay = 2, forget = 4))
print(so.peopleAwareOfSecret(n = 4, delay = 1, forget = 3))




