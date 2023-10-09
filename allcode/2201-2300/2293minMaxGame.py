# 给你一个下标从 0 开始的整数数组 nums ，其长度是 2 的幂。
#
# 对 nums 执行下述算法：
#
# 设 n 等于 nums 的长度，如果 n == 1 ，终止 算法过程。否则，创建 一个新的整数数组 newNums ，新数组长度为 n / 2 ，下标从 0 开始。
# 对于满足 0 <= i < n / 2 的每个 偶数 下标 i ，将 newNums[i] 赋值 为 min(nums[2 * i], nums[2 * i + 1]) 。
# 对于满足 0 <= i < n / 2 的每个 奇数 下标 i ，将 newNums[i] 赋值 为 max(nums[2 * i], nums[2 * i + 1]) 。
# 用 newNums 替换 nums 。
# 从步骤 1 开始 重复 整个过程。
# 执行算法后，返回 nums 中剩下的那个数字。
#
#
#
# 示例 1：
#
#
#
# 输入：nums = [1,3,5,2,4,8,2,2]
# 输出：1
# 解释：重复执行算法会得到下述数组。
# 第一轮：nums = [1,5,4,2]
# 第二轮：nums = [1,4]
# 第三轮：nums = [1]
# 1 是最后剩下的那个数字，返回 1 。
# 示例 2：
#
# 输入：nums = [3]
# 输出：3
# 解释：3 就是最后剩下的数字，返回 3 。
#
#
# 提示：
#
# 1 <= nums.length <= 1024
# 1 <= nums[i] <= 109
# nums.length 是 2 的幂


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
    def minMaxGame1(self, nums: List[int]) -> int:
        def helper(nums):
            ans = []
            for i in range(len(nums) // 2):
                if i % 2 == 0:
                    ans.append(min(nums[i * 2], nums[i * 2 + 1]))
                else:
                    ans.append(max(nums[i * 2], nums[i * 2 + 1]))
            return ans
        while len(nums) > 1:
            nums = helper(nums)
            print(nums)
        return nums[0]
    def minMaxGame(self, nums: List[int]) -> int:
        def f(nms):
            n = len(nms) // 2
            res = [0] * n
            for i in range(n):
                if i & 1:
                    res[i] = max(nms[2 * i], nms[2 * i + 1])
                else:
                    res[i] = min(nms[2 * i], nms[2 * i + 1])
            return res

        while True:
            ans = f(nums)
            print(ans, len(ans))
            if len(ans) == 1:
                return ans[0]
            nums = ans



so = Solution()
print(so.minMaxGame([1,3,5,2,4,8,2,2]))
print(so.minMaxGame([3]))




