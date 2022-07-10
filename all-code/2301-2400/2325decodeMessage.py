# 给你字符串 key 和 message ，分别表示一个加密密钥和一段加密消息。解密 message 的步骤如下：
#
# 使用 key 中 26 个英文小写字母第一次出现的顺序作为替换表中的字母 顺序 。
# 将替换表与普通英文字母表对齐，形成对照表。
# 按照对照表 替换 message 中的每个字母。
# 空格 ' ' 保持不变。
# 例如，key = "happy boy"（实际的加密密钥会包含字母表中每个字母 至少一次），据此，可以得到部分对照表（'h' -> 'a'、'a' -> 'b'、'p' -> 'c'、'y' -> 'd'、'b' -> 'e'、'o' -> 'f'）。
# 返回解密后的消息。
#
#  
#
# 示例 1：
#
#
#
# 输入：key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
# 输出："this is a secret"
# 解释：对照表如上图所示。
# 提取 "the quick brown fox jumps over the lazy dog" 中每个字母的首次出现可以得到替换表。
# 示例 2：
#
#
#
# 输入：key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
# 输出："the five boxing wizards jump quickly"
# 解释：对照表如上图所示。
# 提取 "eljuxhpwnyrdgtqkviszcfmabo" 中每个字母的首次出现可以得到替换表。
#  
#
# 提示：
#
# 26 <= key.length <= 2000
# key 由小写英文字母及 ' ' 组成
# key 包含英文字母表中每个字符（'a' 到 'z'）至少一次
# 1 <= message.length <= 2000
# message 由小写英文字母和 ' ' 组成


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
    def decodeMessage(self, key: str, message: str) -> str:
        key = key.replace(' ', '')
        # print(key)
        d = {' ': ' '}
        i = 0
        for e in key:
            if e not in d:
                d[e] = chr(ord('a') + i)
                i += 1
        # print(d)
        ans = ''
        for s in message:
            ans += d[s]
        return ans



so = Solution()
print(so.decodeMessage(key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"))
print(so.decodeMessage(key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"))




