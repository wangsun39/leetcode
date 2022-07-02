# 给你一个下标从 0 开始长度为 n 的整数数组 nums 。
# 如果以下描述为真，那么 nums 在下标 i 处有一个 合法的分割 ：
#
# 前 i + 1 个元素的和 大于等于 剩下的 n - i - 1 个元素的和。
# 下标 i 的右边 至少有一个 元素，也就是说下标 i 满足 0 <= i < n - 1 。
# 请你返回 nums 中的 合法分割 方案数。
#
#  
#
# 示例 1：
#
# 输入：nums = [10,4,-8,7]
# 输出：2
# 解释：
# 总共有 3 种不同的方案可以将 nums 分割成两个非空的部分：
# - 在下标 0 处分割 nums 。那么第一部分为 [10] ，和为 10 。第二部分为 [4,-8,7] ，和为 3 。因为 10 >= 3 ，所以 i = 0 是一个合法的分割。
# - 在下标 1 处分割 nums 。那么第一部分为 [10,4] ，和为 14 。第二部分为 [-8,7] ，和为 -1 。因为 14 >= -1 ，所以 i = 1 是一个合法的分割。
# - 在下标 2 处分割 nums 。那么第一部分为 [10,4,-8] ，和为 6 。第二部分为 [7] ，和为 7 。因为 6 < 7 ，所以 i = 2 不是一个合法的分割。
# 所以 nums 中总共合法分割方案受为 2 。
# 示例 2：
#
# 输入：nums = [2,3,1,0]
# 输出：2
# 解释：
# 总共有 2 种 nums 的合法分割：
# - 在下标 1 处分割 nums 。那么第一部分为 [2,3] ，和为 5 。第二部分为 [1,0] ，和为 1 。因为 5 >= 1 ，所以 i = 1 是一个合法的分割。
# - 在下标 2 处分割 nums 。那么第一部分为 [2,3,1] ，和为 6 。第二部分为 [0] ，和为 0 。因为 6 >= 0 ，所以 i = 2 是一个合法的分割。
#  
#
# 提示：
#
# 2 <= nums.length <= 105
# -105 <= nums[i] <= 105


# Map = [['U' for _ in range(n)] for _ in range(m)]

from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)

from functools import lru_cache
from typing import List
# @lru_cache(None)

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        s1, s2 = 0, sum(nums)
        ans = 0
        for i in range(n - 1):
            s1 += nums[i]
            s2 -= nums[i]
            if s1 >= s2:
                ans += 1
        return ans



so = Solution()
print(so.waysToSplitArray([10,4,-8,7]))
print(so.waysToSplitArray([2,3,1,0]))




