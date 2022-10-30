# 给你两个字符串数组 creators 和 ids ，和一个整数数组 views ，所有数组的长度都是 n 。平台上第 i 个视频者是 creator[i] ，视频分配的 id 是 ids[i] ，且播放量为 views[i] 。
#
# 视频创作者的 流行度 是该创作者的 所有 视频的播放量的 总和 。请找出流行度 最高 创作者以及该创作者播放量 最大 的视频的 id 。
#
# 如果存在多个创作者流行度都最高，则需要找出所有符合条件的创作者。
# 如果某个创作者存在多个播放量最高的视频，则只需要找出字典序最小的 id 。
# 返回一个二维字符串数组 answer ，其中 answer[i] = [creatori, idi] 表示 creatori 的流行度 最高 且其最流行的视频 id 是 idi ，可以按任何顺序返回该结果。
#
#
#
# 示例 1：
#
# 输入：creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4]
# 输出：[["alice","one"],["bob","two"]]
# 解释：
# alice 的流行度是 5 + 5 = 10 。
# bob 的流行度是 10 。
# chris 的流行度是 4 。
# alice 和 bob 是流行度最高的创作者。
# bob 播放量最高的视频 id 为 "two" 。
# alice 播放量最高的视频 id 是 "one" 和 "three" 。由于 "one" 的字典序比 "three" 更小，所以结果中返回的 id 是 "one" 。
# 示例 2：
#
# 输入：creators = ["alice","alice","alice"], ids = ["a","b","c"], views = [1,2,2]
# 输出：[["alice","b"]]
# 解释：
# id 为 "b" 和 "c" 的视频都满足播放量最高的条件。
# 由于 "b" 的字典序比 "c" 更小，所以结果中返回的 id 是 "b" 。
#
#
# 提示：
#
# n == creators.length == ids.length == views.length
# 1 <= n <= 105
# 1 <= creators[i].length, ids[i].length <= 5
# creators[i] 和 ids[i] 仅由小写英文字母组成
# 0 <= views[i] <= 105
# https://leetcode.cn/problems/most-popular-video-creator/

from typing import List
from typing import Optional
from cmath import inf
from collections import deque
from itertools import pairwise
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
# heap.heapify(nums) # 小顶堆
# heapq.heappop() 函数弹出堆中最小值
# heapq.heappush(nums, 1)
# heapq.heapreplace(heap, item)  删除最小值并添加新值
# 如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache, cache
from typing import List
# @lru_cache(None)

# bit位 函数：
# n.bit_length()  数值的二进制的长度数
# value = int(s, 2)
# lowbit(i) 即i&-i	返回i的最后一位1
# n>>k & 1	求n的第k位数字
# x | (1 << k)	将x第k位 置为1
# x ^ (1 << k)	将x第k位取反
# x & (x - 1)	将x最右边的1置为0(去掉最右边的1)
# x | (x + 1)	将x最右边的0置为1
# x & 1	判断奇偶性 真为奇，假为偶


import string
# string.digits  表示 0123456789
# string.letters：包含所有字母(大写或小写字符串，在python3.0中，使用string.ascii-letters代替)
# string.ascii_lowercase：包含所有小写字母的字符串
# string.printable：包含所有可打印字符的字符串
# string.punctuation：包含所有标点的字符串
# string.uppercase：包含所有大写字母的字符串

# f-string用法
# name = 'sun'
# f"Hello, my name is {name}"

from itertools import accumulate
# s = list(accumulate(nums, initial=0))  # 计算前缀和


class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        n = len(creators)
        d = defaultdict(int)
        d2 = {}
        max_num = 0
        max_set = set()
        for i in range(n):
            d[creators[i]] += views[i]
            if creators[i] not in d2:
                d2[creators[i]] = i
            else:
                if views[i] > views[d2[creators[i]]]:
                    d2[creators[i]] = i
                elif views[i] == views[d2[creators[i]]]:
                    if ids[i] < ids[d2[creators[i]]]:
                        d2[creators[i]] = i
            if d[creators[i]] > max_num:
                max_num = d[creators[i]]
                max_set = set()
                max_set.add(creators[i])
            elif d[creators[i]] == max_num:
                max_set.add(creators[i])
        ans = []
        # print(max_set)
        # print(d2)
        for cr in max_set:
            ans.append([cr, ids[d2[cr]]])
        return ans


so = Solution()
print(so.mostPopularCreator(creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4]))
print(so.mostPopularCreator(creators = ["alice","alice","alice"], ids = ["a","b","c"], views = [1,2,2]))




