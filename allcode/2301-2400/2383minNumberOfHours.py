# 你正在参加一场比赛，给你两个 正 整数 initialEnergy 和 initialExperience 分别表示你的初始精力和初始经验。
#
# 另给你两个下标从 0 开始的整数数组 energy 和 experience，长度均为 n 。
#
# 你将会 依次 对上 n 个对手。第 i 个对手的精力和经验分别用 energy[i] 和 experience[i] 表示。当你对上对手时，需要在经验和精力上都 严格 超过对手才能击败他们，然后在可能的情况下继续对上下一个对手。
#
# 击败第 i 个对手会使你的经验 增加 experience[i]，但会将你的精力 减少 energy[i] 。
#
# 在开始比赛前，你可以训练几个小时。每训练一个小时，你可以选择将增加经验增加 1 或者 将精力增加 1 。
#
# 返回击败全部 n 个对手需要训练的 最少 小时数目。
#
#
#
# 示例 1：
#
# 输入：initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1]
# 输出：8
# 解释：在 6 小时训练后，你可以将精力提高到 11 ，并且再训练 2 个小时将经验提高到 5 。
# 按以下顺序与对手比赛：
# - 你的精力与经验都超过第 0 个对手，所以获胜。
#   精力变为：11 - 1 = 10 ，经验变为：5 + 2 = 7 。
# - 你的精力与经验都超过第 1 个对手，所以获胜。
#   精力变为：10 - 4 = 6 ，经验变为：7 + 6 = 13 。
# - 你的精力与经验都超过第 2 个对手，所以获胜。
#   精力变为：6 - 3 = 3 ，经验变为：13 + 3 = 16 。
# - 你的精力与经验都超过第 3 个对手，所以获胜。
#   精力变为：3 - 2 = 1 ，经验变为：16 + 1 = 17 。
# 在比赛前进行了 8 小时训练，所以返回 8 。
# 可以证明不存在更小的答案。
# 示例 2：
#
# 输入：initialEnergy = 2, initialExperience = 4, energy = [1], experience = [3]
# 输出：0
# 解释：你不需要额外的精力和经验就可以赢得比赛，所以返回 0 。
#
#
# 提示：
#
# n == energy.length == experience.length
# 1 <= n <= 100
# 1 <= initialEnergy, initialExperience, energy[i], experience[i] <= 100


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

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        n = len(energy)

        sum1 = sum(energy)
        if initialEnergy <= sum1:
            e1 = sum1 - initialEnergy + 1
        else:
            e1 = 0
        e2 = 0
        for i in range(n):
            if initialExperience <= experience[i]:
                e2 = max(e2, experience[i] - initialExperience + 1)
            initialExperience += experience[i]
        return e1 + e2



so = Solution()
print(so.minNumberOfHours(1,1,[1,1,1,1],[1,1,1,50]))
print(so.minNumberOfHours(initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1]))
print(so.minNumberOfHours(initialEnergy = 2, initialExperience = 4, energy = [1], experience = [3]))




