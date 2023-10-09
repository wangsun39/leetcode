# 给你一个下标从 0 开始的二维整数数组 brackets ，其中 brackets[i] = [upperi, percenti] ，表示第 i 个税级的上限是 upperi ，征收的税率为 percenti 。税级按上限 从低到高排序（在满足 0 < i < brackets.length 的前提下，upperi-1 < upperi）。
#
# 税款计算方式如下：
#
# 不超过 upper0 的收入按税率 percent0 缴纳
# 接着 upper1 - upper0 的部分按税率 percent1 缴纳
# 然后 upper2 - upper1 的部分按税率 percent2 缴纳
# 以此类推
# 给你一个整数 income 表示你的总收入。返回你需要缴纳的税款总额。与标准答案误差不超 10-5 的结果将被视作正确答案。
#
#
#
# 示例 1：
#
# 输入：brackets = [[3,50],[7,10],[12,25]], income = 10
# 输出：2.65000
# 解释：
# 前 $3 的税率为 50% 。需要支付税款 $3 * 50% = $1.50 。
# 接下来 $7 - $3 = $4 的税率为 10% 。需要支付税款 $4 * 10% = $0.40 。
# 最后 $10 - $7 = $3 的税率为 25% 。需要支付税款 $3 * 25% = $0.75 。
# 需要支付的税款总计 $1.50 + $0.40 + $0.75 = $2.65 。
# 示例 2：
#
# 输入：brackets = [[1,0],[4,25],[5,50]], income = 2
# 输出：0.25000
# 解释：
# 前 $1 的税率为 0% 。需要支付税款 $1 * 0% = $0 。
# 剩下 $1 的税率为 25% 。需要支付税款 $1 * 25% = $0.25 。
# 需要支付的税款总计 $0 + $0.25 = $0.25 。
# 示例 3：
#
# 输入：brackets = [[2,50]], income = 0
# 输出：0.00000
# 解释：
# 没有收入，无需纳税，需要支付的税款总计 $0 。
#
#
# 提示：
#
# 1 <= brackets.length <= 100
# 1 <= upperi <= 1000
# 0 <= percenti <= 100
# 0 <= income <= 1000
# upperi 按递增顺序排列
# upperi 中的所有值 互不相同
# 最后一个税级的上限大于等于 income

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
    def calculateTax1(self, brackets: List[List[int]], income: int) -> float:
        ans = 0
        brackets.insert(0, [0, 0])
        for i, [upper, tax] in enumerate(brackets[1:], 1):
            if upper < income:
                ans += (upper - brackets[i - 1][0]) * tax
            else:
                ans += (income - brackets[i - 1][0]) * tax
                break
        return ans / 100  # 浮点运算放在最后

    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        brackets.insert(0, [0, 0])
        pos = bisect.bisect_left(brackets, income, key=lambda x: x[0])
        ans = (income - brackets[pos - 1][0]) * brackets[pos][1]
        for i in range(pos - 1, 0, -1):
            ans += (brackets[i][0] - brackets[i - 1][0]) * brackets[i][1]
        return ans / 100  # 浮点运算放在最后




so = Solution()
print(so.calculateTax(brackets = [[3,50],[7,10],[12,25]], income = 10))
print(so.calculateTax(brackets = [[1,0],[4,25],[5,50]], income = 2))
print(so.calculateTax(brackets = [[2,50]], income = 0))




