# 给你一个整数数组 nums 和一个整数 k 。你可以将 nums 划分成一个或多个 子序列 ，使 nums 中的每个元素都 恰好 出现在一个子序列中。
#
# 在满足每个子序列中最大值和最小值之间的差值最多为 k 的前提下，返回需要划分的 最少 子序列数目。
#
# 子序列 本质是一个序列，可以通过删除另一个序列中的某些元素（或者不删除）但不改变剩下元素的顺序得到。
#
#
#
# 示例 1：
#
# 输入：nums = [3,6,1,2,5], k = 2
# 输出：2
# 解释：
# 可以将 nums 划分为两个子序列 [3,1,2] 和 [6,5] 。
# 第一个子序列中最大值和最小值的差值是 3 - 1 = 2 。
# 第二个子序列中最大值和最小值的差值是 6 - 5 = 1 。
# 由于创建了两个子序列，返回 2 。可以证明需要划分的最少子序列数目就是 2 。
# 示例 2：
#
# 输入：nums = [1,2,3], k = 1
# 输出：2
# 解释：
# 可以将 nums 划分为两个子序列 [1,2] 和 [3] 。
# 第一个子序列中最大值和最小值的差值是 2 - 1 = 1 。
# 第二个子序列中最大值和最小值的差值是 3 - 3 = 0 。
# 由于创建了两个子序列，返回 2 。注意，另一种最优解法是将 nums 划分成子序列 [1] 和 [2,3] 。
# 示例 3：
#
# 输入：nums = [2,2,4,5], k = 0
# 输出：3
# 解释：
# 可以将 nums 划分为三个子序列 [2,2]、[4] 和 [5] 。
# 第一个子序列中最大值和最小值的差值是 2 - 2 = 0 。
# 第二个子序列中最大值和最小值的差值是 4 - 4 = 0 。
# 第三个子序列中最大值和最小值的差值是 5 - 5 = 0 。
# 由于创建了三个子序列，返回 3 。可以证明需要划分的最少子序列数目就是 3 。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 105
# 0 <= k <= 105

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
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        curL, curH = nums[0], nums[0]
        for e in nums[1:]:
            if abs(e - curL) <= k and abs(e - curH) <= k:
                curL, curH = min(curL, e), max(curH, e)
            else:
                curL, curH = e, e
                ans += 1
        return ans


so = Solution()
print(so.partitionArray(nums = [3,6,1,2,5], k = 2))
print(so.partitionArray(nums = [1,2,3], k = 1))
print(so.partitionArray(nums = [2,2,4,5], k = 0))




