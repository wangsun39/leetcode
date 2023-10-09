# 给定 N 个无限容量且初始均空的水缸，每个水缸配有一个水桶用来打水，第 i 个水缸配备的水桶容量记作 bucket[i]。小扣有以下两种操作：
#
# 升级水桶：选择任意一个水桶，使其容量增加为 bucket[i]+1
# 蓄水：将全部水桶接满水，倒入各自对应的水缸
# 每个水缸对应最低蓄水量记作 vat[i]，返回小扣至少需要多少次操作可以完成所有水缸蓄水要求。
#
# 注意：实际蓄水量 达到或超过 最低蓄水量，即完成蓄水要求。
#
# 示例 1：
#
# 输入：bucket = [1,3], vat = [6,8]
#
# 输出：4
#
# 解释：
# 第 1 次操作升级 bucket[0]；
# 第 2 ~ 4 次操作均选择蓄水，即可完成蓄水要求。
# vat1.gif
#
# 示例 2：
#
# 输入：bucket = [9,0,1], vat = [0,2,2]
#
# 输出：3
#
# 解释：
# 第 1 次操作均选择升级 bucket[1]
# 第 2~3 次操作选择蓄水，即可完成蓄水要求。
#
# 提示：
#
# 1 <= bucket.length == vat.length <= 100
# 0 <= bucket[i], vat[i] <= 10^4
from math import inf
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

class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        n = len(bucket)
        if all(x == 0 for x in vat):
            return 0

        def func(oper2):  # 给定蓄水总次数，求总操作次数
            oper1 = sum(max((vat[i] + oper2 - 1) // oper2 - bucket[i], 0) for i in range(n))
            return oper1 + oper2

        ans = inf
        up = max(vat)
        for x in range(1, up + 1):
            ans = min(ans, func(x))

        return ans


so = Solution()
print(so.storeWater([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000]))
print(so.storeWater([3,2,5], [0,0,0]))
print(so.storeWater(bucket = [1,3], vat = [6,8]))
print(so.storeWater(bucket = [9,0,1], vat = [0,2,2]))




