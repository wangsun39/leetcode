# 「力扣挑战赛」 的入场仪式马上就要开始了，由于安保工作的需要，设置了可容纳人数总和为 M 的 N 个安检室，capacities[i] 记录第 i 个安检室可容纳人数。安检室拥有两种类型：
#
# 先进先出：在安检室中的所有观众中，最早进入安检室的观众最先离开
# 后进先出：在安检室中的所有观众中，最晚进入安检室的观众最先离开
#
#
# 恰好 M+1 位入场的观众（编号从 0 开始）需要排队依次入场安检， 入场安检的规则如下：
#
# 观众需要先进入编号 0 的安检室
# 当观众将进入编号 i 的安检室时（0 <= i < N)，
# 若安检室未到达可容纳人数上限，该观众可直接进入；
# 若安检室已到达可容纳人数上限，在该观众进入安检室之前需根据当前安检室类型选择一位观众离开后才能进入；
# 当观众离开编号 i 的安检室时 （0 <= i < N-1)，将进入编号 i+1 的安检室接受安检。
# 若可以任意设定每个安检室的类型，请问有多少种设定安检室类型的方案可以使得编号 k 的观众第一个通过最后一个安检室入场。
#
# 注意：
#
# 观众不可主动离开安检室，只有当安检室容纳人数达到上限，且又有新观众需要进入时，才可根据安检室的类型选择一位观众离开；
# 由于方案数可能过大，请将答案对 1000000007 取模后返回。
# 示例 1：
#
# 输入：capacities = [2,2,3], k = 2
#
# 输出：2
# 解释：
# 存在两种设定的 2 种方案：
#
# 方案 1：将编号为 0 、1 的实验室设置为 后进先出 的类型，编号为 2 的实验室设置为 先进先出 的类型；
# 方案 2：将编号为 0 、1 的实验室设置为 先进先出 的类型，编号为 2 的实验室设置为 后进先出 的类型。
# 以下是方案 1 的示意图：
#
#
# 示例 2：
#
# 输入：capacities = [3,3], k = 3
#
# 输出：0
#
# 示例 3：
#
# 输入：capacities = [4,3,2,2], k = 6
#
# 输出：2
#
# 提示:
#
# 1 <= capacities.length <= 200
# 1 <= capacities[i] <= 200
# 0 <= k <= sum(capacities)
#
# https://leetcode.cn/problems/oPs9Bm



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

from functools import lru_cache, cache
from typing import List
# @lru_cache(None)

class Solution:
    def securityCheck(self, capacities: List[int], k: int) -> int:
        MOD = 1000000007
        n = len(capacities)
        pre = [capacities[0]]  # 前缀和
        for i in range(1, n):
            pre.append(pre[-1] + capacities[i])
        @cache
        def dfs(epos, i):  # epos: 经过i安检后期望的排位，i: 在第i个安检处
            if epos + pre[i] < k:  # 剪枝
                return 0
            ans = 0
            if i == 0:
                if epos == k:
                    ans += 1
                if epos + capacities[i] == k + 1:
                    ans += 1
                return ans
            ans = dfs(epos, i - 1)
            if epos + capacities[i] - 1 <= k:
                ans += dfs(epos + capacities[i] - 1, i - 1)
                ans %= MOD
            return ans
        ans = dfs(0, n - 1)
        return ans


so = Solution()
print(so.securityCheck([30,18,23,26,20,29,5,10,4,24,3,29,28,22,11,16,18], 51))  # 72
print(so.securityCheck([98,163,11,75,142,111,9,175,106,69,97,187,54,89,35,34,29,157,92,43,8,111,148,102,119,20,165,182,182,175,20,200,109,140,186,142,36,44,40,54,43,59,8,135,35,127,92,160,189,74,184,86,176,31,105,198,68,41,88,161,129,85,137,178,38,97,190,191,143,79,61,97,89,100,121,131,79,105,105,26,175,40,38,2,150,153,163,181,133,28,179,200,166,179,53,153,165,155,132,29,69,177,188,158,44,97,22,10,3,30,93,185,124,82,28,174,116,95,150,179,65,171,125,199,59,41,144,142,20,200,131,44,7,165,43,133,105,156,170,54,113,182,176,104,68,6,151,35,100,44,113,145,14,97,23,165,151,104,86,60,130,117,11,123,159,27,69,130],
16065))  # 2
print(so.securityCheck(capacities = [4,3,2,2], k = 6))  # 2
print(so.securityCheck(capacities = [3,3], k = 3))  # 0
print(so.securityCheck(capacities = [2,2,3], k = 2))  # 2

