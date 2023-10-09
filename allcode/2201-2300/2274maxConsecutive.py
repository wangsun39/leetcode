# Alice 管理着一家公司，并租用大楼的部分楼层作为办公空间。Alice 决定将一些楼层作为 特殊楼层 ，仅用于放松。
#
# 给你两个整数 bottom 和 top ，表示 Alice 租用了从 bottom 到 top（含 bottom 和 top 在内）的所有楼层。另给你一个整数数组 special ，其中 special[i] 表示  Alice 指定用于放松的特殊楼层。
#
# 返回不含特殊楼层的 最大 连续楼层数。
#
#  
#
# 示例 1：
#
# 输入：bottom = 2, top = 9, special = [4,6]
# 输出：3
# 解释：下面列出的是不含特殊楼层的连续楼层范围：
# - (2, 3) ，楼层数为 2 。
# - (5, 5) ，楼层数为 1 。
# - (7, 9) ，楼层数为 3 。
# 因此，返回最大连续楼层数 3 。
# 示例 2：
#
# 输入：bottom = 6, top = 8, special = [7,6,8]
# 输出：0
# 解释：每层楼都被规划为特殊楼层，所以返回 0 。
#  
#
# 提示
#
# 1 <= special.length <= 105
# 1 <= bottom <= special[i] <= top <= 109
# special 中的所有值 互不相同


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
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        ans = 0
        if special[0] != bottom:
            ans = max(ans, special[0] - bottom)
            special.insert(0, bottom)
        if special[-1] != top:
            ans = max(ans, top - special[-1])
            special.append(top)
        n = len(special) - 1
        for i in range(1, n + 1):
            num = special[i] - special[i - 1] - 1
            ans = max(num, ans)
        return ans



so = Solution()
print(so.maxConsecutive(bottom = 1, top = 49, special = [11,12,22,49,4,6]))
print(so.maxConsecutive(bottom = 6, top = 6, special = [6]))
print(so.maxConsecutive(bottom = 6, top = 8, special = [7,6,8]))
print(so.maxConsecutive(bottom = 2, top = 9, special = [4,6]))




