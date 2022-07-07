# 给你一个下标从 0 开始的整数数组 nums 。一次操作中，选择 任意 非负整数 x 和一个下标 i ，更新 nums[i] 为 nums[i] AND (nums[i] XOR x) 。
#
# 注意，AND 是逐位与运算，XOR 是逐位异或运算。
#
# 请你执行 任意次 更新操作，并返回 nums 中所有元素 最大 逐位异或和。
#
#  
#
# 示例 1：
#
# 输入：nums = [3,2,4,6]
# 输出：7
# 解释：选择 x = 4 和 i = 3 进行操作，num[3] = 6 AND (6 XOR 4) = 6 AND 2 = 2 。
# 现在，nums = [3, 2, 4, 2] 且所有元素逐位异或得到 3 XOR 2 XOR 4 XOR 2 = 7 。
# 可知 7 是能得到的最大逐位异或和。
# 注意，其他操作可能也能得到逐位异或和 7 。
# 示例 2：
#
# 输入：nums = [1,2,3,9,2]
# 输出：11
# 解释：执行 0 次操作。
# 所有元素的逐位异或和为 1 XOR 2 XOR 3 XOR 9 XOR 2 = 11 。
# 可知 11 是能得到的最大逐位异或和。
#  
#
# 提示：
#
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 108


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

# bit位 函数：
# n.bit_length()
# value = int(s, 2)
from functools import reduce
class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        ans = 0
        for e in nums:
            ans |= e
        return ans

        # return reduce(or_, nums)



so = Solution()
print(so.maximumXOR([3,2,4,6]))
print(so.maximumXOR([1,2,3,9,2]))




