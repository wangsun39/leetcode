# 在 「力扣挑战赛」 开幕式的压轴节目 「无人机方阵」中，每一架无人机展示一种灯光颜色。 无人机方阵通过两种操作进行颜色图案变换：
#
# 调整无人机的位置布局
# 切换无人机展示的灯光颜色
# 给定两个大小均为 N*M 的二维数组 source 和 target 表示无人机方阵表演的两种颜色图案，由于无人机切换灯光颜色的耗能很大，请返回从 source 到 target 最少需要多少架无人机切换灯光颜色。
#
# 注意： 调整无人机的位置布局时无人机的位置可以随意变动。
#
# 示例 1：
#
# 输入：source = [[1,3],[5,4]], target = [[3,1],[6,5]]
#
# 输出：1
#
# 解释：
# 最佳方案为
# 将 [0,1] 处的无人机移动至 [0,0] 处；
# 将 [0,0] 处的无人机移动至 [0,1] 处；
# 将 [1,0] 处的无人机移动至 [1,1] 处；
# 将 [1,1] 处的无人机移动至 [1,0] 处，其灯光颜色切换为颜色编号为 6 的灯光；
# 因此从source 到 target 所需要的最少灯光切换次数为 1。
#
#
# 示例 2：
#
# 输入：source = [[1,2,3],[3,4,5]], target = [[1,3,5],[2,3,4]]
#
# 输出：0
# 解释：
# 仅需调整无人机的位置布局，便可完成图案切换。因此不需要无人机切换颜色
#
# 提示：
# n == source.length == target.length
# m == source[i].length == target[i].length
# 1 <= n, m <=100
# 1 <= source[i][j], target[i][j] <=10^4


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
    def minimumSwitchingTimes(self, source: List[List[int]], target: List[List[int]]) -> int:
        s1, s2 = [], []
        for s in source:
            s1 += s
        for t in target:
            s2 += t
        c1, c2 = Counter(s1), Counter(s2)
        ans = 0
        for k in c1:
            ans += max(c1[k] - c2[k], 0)
        return ans


so = Solution()
print(so.minimumSwitchingTimes(source = [[1,3],[5,4]], target = [[3,1],[6,5]]))
print(so.minimumSwitchingTimes(source = [[1,2,3],[3,4,5]], target = [[1,3,5],[2,3,4]]))




