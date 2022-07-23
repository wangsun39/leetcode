# 给定一个长度为 n 的整数数组 nums ，其中 nums 是范围为 [1，n] 的整数的排列。还提供了一个 2D 整数数组 sequences ，其中 sequences[i] 是 nums 的子序列。
# 检查 nums 是否是唯一的最短 超序列 。最短 超序列 是 长度最短 的序列，并且所有序列 sequences[i] 都是它的子序列。对于给定的数组 sequences ，可能存在多个有效的 超序列 。
#
# 例如，对于 sequences = [[1,2],[1,3]] ，有两个最短的 超序列 ，[1,2,3] 和 [1,3,2] 。
# 而对于 sequences = [[1,2],[1,3],[1,2,3]] ，唯一可能的最短 超序列 是 [1,2,3] 。[1,2,3,4] 是可能的超序列，但不是最短的。
# 如果 nums 是序列的唯一最短 超序列 ，则返回 true ，否则返回 false 。
# 子序列 是一个可以通过从另一个序列中删除一些元素或不删除任何元素，而不改变其余元素的顺序的序列。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,3], sequences = [[1,2],[1,3]]
# 输出：false
# 解释：有两种可能的超序列：[1,2,3]和[1,3,2]。
# 序列 [1,2] 是[1,2,3]和[1,3,2]的子序列。
# 序列 [1,3] 是[1,2,3]和[1,3,2]的子序列。
# 因为 nums 不是唯一最短的超序列，所以返回false。
# 示例 2：
#
# 输入：nums = [1,2,3], sequences = [[1,2]]
# 输出：false
# 解释：最短可能的超序列为 [1,2]。
# 序列 [1,2] 是它的子序列：[1,2]。
# 因为 nums 不是最短的超序列，所以返回false。
# 示例 3：
#
# 输入：nums = [1,2,3], sequences = [[1,2],[1,3],[2,3]]
# 输出：true
# 解释：最短可能的超序列为[1,2,3]。
# 序列 [1,2] 是它的一个子序列：[1,2,3]。
# 序列 [1,3] 是它的一个子序列：[1,2,3]。
# 序列 [2,3] 是它的一个子序列：[1,2,3]。
# 因为 nums 是唯一最短的超序列，所以返回true。
#  
#
# 提示：
#
# n == nums.length
# 1 <= n <= 104
# nums 是 [1, n] 范围内所有整数的排列
# 1 <= sequences.length <= 104
# 1 <= sequences[i].length <= 104
# 1 <= sum(sequences[i].length) <= 105
# 1 <= sequences[i][j] <= n
# sequences 的所有数组都是 唯一 的
# sequences[i] 是 nums 的一个子序列




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
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)

        d = {nums[i]: i + 1 for i in range(n)}
        seq = [[0 for _ in range(len(sequences[i]))] for i in range(len(sequences))]
        for i in range(len(sequences)):
            for j in range(len(sequences[i])):
                seq[i][j] = d[sequences[i][j]]
        def find(x, y):
            m = len(seq)
            for i in range(m):
                pos = bisect.bisect_left(seq[i], x)
                if pos + 1 < len(seq[i]) and seq[i][pos] == x and seq[i][pos + 1] == y:
                    return True
            return False
        nu = [i + 1 for i in range(n)]
        for i in range(n - 1):
            if not find(nu[i], nu[i + 1]):
                return False
        return True




so = Solution()
print(so.sequenceReconstruction([5,4,8,9,1,6,3,2,7,10], [[8,9,1],[6,3,2,7,10],[5,4]]))
print(so.sequenceReconstruction([1,2,3,4,5], [[1,2,3,4,5],[1,2,3,4],[1,2,3],[1],[4],[5]]))
print(so.sequenceReconstruction(nums = [4,1,5,2,6,3], sequences = [[5,2,6,3],[4,1,5,2]]))
print(so.sequenceReconstruction(nums = [1,2,3], sequences = [[1,2],[1,3],[2,3]]))
print(so.sequenceReconstruction(nums = [1,2,3], sequences = [[1,2],[1,3]]))
print(so.sequenceReconstruction(nums = [1,2,3], sequences = [[1,2]]))




