# 给定一个未排序的整数数组
# nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
# 请你设计并实现时间复杂度为
# O(n)
# 的算法解决此问题。
#
#
#
# 示例
# 1：
#
# 输入：nums = [100, 4, 200, 1, 3, 2]
# 输出：4
# 解释：最长数字连续序列是[1, 2, 3, 4]。它的长度为
# 4。
# 示例
# 2：
#
# 输入：nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# 输出：9
#
# 提示：
#
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109



from typing import List
import time
from collections import deque

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        n = len(nums)
        fa = {nums[i]: nums[i] for i in range(n)}  # 存放每个点所在连通块的代表元（未必每个点的fa值都是最新的，调用find获取，不要直接fa[i]获取）

        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]

        ans = 0
        for x in nums:
            fa[x] = x
            if x + 1 in s:
                fa[x] = find(x + 1)
            if x - 1 in s:
                fa[x - 1] = fa[x]
        for x in nums:
            fa[x] = find(x)
            ans = max(ans, fa[x] - x + 1)
        print(fa)
        return ans


so = Solution()

print(so.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(so.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))


