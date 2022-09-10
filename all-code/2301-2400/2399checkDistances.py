# 给你一个下标从 0 开始的字符串 s ，该字符串仅由小写英文字母组成，s 中的每个字母都 恰好 出现 两次 。另给你一个下标从 0 开始、长度为 26 的的整数数组 distance 。
#
# 字母表中的每个字母按从 0 到 25 依次编号（即，'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25）。
#
# 在一个 匀整 字符串中，第 i 个字母的两次出现之间的字母数量是 distance[i] 。如果第 i 个字母没有在 s 中出现，那么 distance[i] 可以 忽略 。
#
# 如果 s 是一个 匀整 字符串，返回 true ；否则，返回 false 。
#
#  
#
# 示例 1：
#
# 输入：s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# 输出：true
# 解释：
# - 'a' 在下标 0 和下标 2 处出现，所以满足 distance[0] = 1 。
# - 'b' 在下标 1 和下标 5 处出现，所以满足 distance[1] = 3 。
# - 'c' 在下标 3 和下标 4 处出现，所以满足 distance[2] = 0 。
# 注意 distance[3] = 5 ，但是由于 'd' 没有在 s 中出现，可以忽略。
# 因为 s 是一个匀整字符串，返回 true 。
# 示例 2：
#
# 输入：s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# 输出：false
# 解释：
# - 'a' 在下标 0 和 1 处出现，所以两次出现之间的字母数量为 0 。
# 但是 distance[0] = 1 ，s 不是一个匀整字符串。
#  
#
# 提示：
#
# 2 <= s.length <= 52
# s 仅由小写英文字母组成
# s 中的每个字母恰好出现两次
# distance.length == 26
# 0 <= distance[i] <= 50


from typing import List
from typing import Optional
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
import math
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
import heapq
# heap.heapify(nums)
# heapq.heappop() 函数弹出堆中最小值
# heapq.heappush(nums, 1)
# 如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache
from typing import List
# @lru_cache(None)

# bit位 函数：
# n.bit_length()
# value = int(s, 2)

import string
# string.digits  表示 0123456789

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dist = [-1] * 26
        i, n = 0, len(s)
        while i < n:
            if dist[ord(s[i]) - ord('a')] != -1:
                i += 1
                continue
            pos = s.find(s[i], i + 1)
            dist[ord(s[i]) - ord('a')] = pos - i - 1
            if dist[ord(s[i]) - ord('a')] != distance[ord(s[i]) - ord('a')]:
                return False
        # print(dist)
        return True


so = Solution()
print(so.checkDistances(s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
print(so.checkDistances(s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))




