# 作为国王的统治者，你有一支巫师军队听你指挥。
#
# 给你一个下标从 0 开始的整数数组 strength ，其中 strength[i] 表示第 i 位巫师的力量值。对于连续的一组巫师（也就是这些巫师的力量值是 strength 的 子数组），总力量 定义为以下两个值的 乘积 ：
#
# 巫师中 最弱 的能力值。
# 组中所有巫师的个人力量值 之和 。
# 请你返回 所有 巫师组的 总 力量之和。由于答案可能很大，请将答案对 109 + 7 取余 后返回。
#
# 子数组 是一个数组里 非空 连续子序列。
#
#  
#
# 示例 1：
#
# 输入：strength = [1,3,1,2]
# 输出：44
# 解释：以下是所有连续巫师组：
# - [1,3,1,2] 中 [1] ，总力量值为 min([1]) * sum([1]) = 1 * 1 = 1
# - [1,3,1,2] 中 [3] ，总力量值为 min([3]) * sum([3]) = 3 * 3 = 9
# - [1,3,1,2] 中 [1] ，总力量值为 min([1]) * sum([1]) = 1 * 1 = 1
# - [1,3,1,2] 中 [2] ，总力量值为 min([2]) * sum([2]) = 2 * 2 = 4
# - [1,3,1,2] 中 [1,3] ，总力量值为 min([1,3]) * sum([1,3]) = 1 * 4 = 4
# - [1,3,1,2] 中 [3,1] ，总力量值为 min([3,1]) * sum([3,1]) = 1 * 4 = 4
# - [1,3,1,2] 中 [1,2] ，总力量值为 min([1,2]) * sum([1,2]) = 1 * 3 = 3
# - [1,3,1,2] 中 [1,3,1] ，总力量值为 min([1,3,1]) * sum([1,3,1]) = 1 * 5 = 5
# - [1,3,1,2] 中 [3,1,2] ，总力量值为 min([3,1,2]) * sum([3,1,2]) = 1 * 6 = 6
# - [1,3,1,2] 中 [1,3,1,2] ，总力量值为 min([1,3,1,2]) * sum([1,3,1,2]) = 1 * 7 = 7
# 所有力量值之和为 1 + 9 + 1 + 4 + 4 + 4 + 3 + 5 + 6 + 7 = 44 。
# 示例 2：
#
# 输入：strength = [5,4,6]
# 输出：213
# 解释：以下是所有连续巫师组：
# - [5,4,6] 中 [5] ，总力量值为 min([5]) * sum([5]) = 5 * 5 = 25
# - [5,4,6] 中 [4] ，总力量值为 min([4]) * sum([4]) = 4 * 4 = 16
# - [5,4,6] 中 [6] ，总力量值为 min([6]) * sum([6]) = 6 * 6 = 36
# - [5,4,6] 中 [5,4] ，总力量值为 min([5,4]) * sum([5,4]) = 4 * 9 = 36
# - [5,4,6] 中 [4,6] ，总力量值为 min([4,6]) * sum([4,6]) = 4 * 10 = 40
# - [5,4,6] 中 [5,4,6] ，总力量值为 min([5,4,6]) * sum([5,4,6]) = 4 * 15 = 60
# 所有力量值之和为 25 + 16 + 36 + 36 + 40 + 60 = 213 。
#  
#
# 提示：
#
# 1 <= strength.length <= 105
# 1 <= strength[i] <= 109

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
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)
        M = int(1e9) + 7
        T = [0] * n # 从 sum(strength[i:m])
        Min = [int(1e10)] * n  # 从i 到m - 1的最小值
        T[0] = strength[0]
        Min[0] = strength[0]
        ans = T[0] * T[0]
        for i in range(1, n):

            for j in range(i + 1):
                T[j] += strength[i]
                Min[j] = min(Min[j], strength[i])
                ans += ((T[j] * Min[j]) % M)
                ans %= M
        return ans




so = Solution()
print(so.totalStrength([747,812,112,1230,1426,1477,1388,976,849,1431,1885,1845,1070,1980,280,1075,232,1330,1868,1696,1361,1822,524,1899,1904,538,731,985,279,1608,1558,930,1232,1497,875,1850,1173,805,1720,33,233,330,1429,1688,281,362,1963,927,1688,256,1594,1823,743,553,1633,1898,1101,1278,717,522,1926,1451,119,1283,1016,194,780,1436,1233,710,1608,523,874,1779,1822,134,1984]))
print(so.totalStrength([5,4,6]))
print(so.totalStrength([1,3,1,2]))




