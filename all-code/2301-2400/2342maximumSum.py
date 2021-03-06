# 给你一个下标从 0 开始的数组 nums ，数组中的元素都是 正 整数。请你选出两个下标 i 和 j（i != j），且 nums[i] 的数位和 与  nums[j] 的数位和相等。
#
# 请你找出所有满足条件的下标 i 和 j ，找出并返回 nums[i] + nums[j] 可以得到的 最大值 。
#
#  
#
# 示例 1：
#
# 输入：nums = [18,43,36,13,7]
# 输出：54
# 解释：满足条件的数对 (i, j) 为：
# - (0, 2) ，两个数字的数位和都是 9 ，相加得到 18 + 36 = 54 。
# - (1, 4) ，两个数字的数位和都是 7 ，相加得到 43 + 7 = 50 。
# 所以可以获得的最大和是 54 。
# 示例 2：
#
# 输入：nums = [10,12,19,14]
# 输出：-1
# 解释：不存在满足条件的数对，返回 -1 。
#  
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109


from typing import List
from typing import Optional
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
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

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache
from typing import List
# @lru_cache(None)

# bit位 函数：
# n.bit_length()
# value = int(s, 2)

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sums = []
        for num in nums:
            st = list(str(num))
            digits = sum([int(e) for e in st])
            sums.append(digits)
        # print(sums)
        d = {}
        for idx, s in enumerate(sums):
            if s not in d:
                d[s] = [nums[idx]]
                continue
            if len(d[s]) == 1:
                if d[s][0] < nums[idx]:
                    d[s].append(nums[idx])
                else:
                    d[s].insert(0, nums[idx])
                continue
            if d[s][0] >= nums[idx]:
                continue
            if d[s][1] >= nums[idx]:
                d[s][0] = nums[idx]
                continue
            d[s].pop(0)
            d[s].append(nums[idx])
        # print(d)
        ans = -1
        for key in d:
            if len(d[key]) >= 2:
                ans = max(ans, d[key][0] + d[key][1])
        return ans



so = Solution()
print(so.maximumSum([229,398,269,317,420,464,491,218,439,153,482,169,411,93,147,50,347,210,251,366,401]))
print(so.maximumSum([10,12,19,14]))
print(so.maximumSum([18,43,36,13,7]))




