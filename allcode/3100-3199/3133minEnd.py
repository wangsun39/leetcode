# 给你两个整数 n 和 x 。你需要构造一个长度为 n 的 正整数 数组 nums ，对于所有 0 <= i < n - 1 ，满足 nums[i + 1] 大于 nums[i] ，并且数组 nums 中所有元素的按位 AND 运算结果为 x 。
#
# 返回 nums[n - 1] 可能的 最小 值。
#
#
#
# 示例 1：
#
# 输入：n = 3, x = 4
#
# 输出：6
#
# 解释：
#
# 数组 nums 可以是 [4,5,6] ，最后一个元素为 6 。
#
# 示例 2：
#
# 输入：n = 2, x = 7
#
# 输出：15
#
# 解释：
#
# 数组 nums 可以是 [7,15] ，最后一个元素为 15 。
#
#
#
# 提示：
#
# 1 <= n, x <= 108

import math

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n2 = bin(n - 1)[2:][::-1]
        x2 = bin(x)[2:]
        arr = list(x2)[::-1]
        j = 0
        end = False
        for i in range(len(n2)):
            if end:
                arr.append(n2[i])
                continue
            while j < len(arr) and arr[j] == '1':
                j += 1
            if j < len(arr):
                arr[j] = n2[i]
                j += 1
            else:
                arr.append(n2[i])
                end = True
        res = ''.join(arr[::-1])
        return int(res, 2)



so = Solution()
print(so.minEnd(n = 3, x = 4))
print(so.minEnd(n = 2, x = 7))




