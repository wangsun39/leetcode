# 给你一个正整数数组 arr（可能存在重复的元素），请你返回可在 一次交换（交换两数字 arr[i] 和 arr[j] 的位置）后得到的、按字典序排列小于 arr 的最大排列。
#
# 如果无法这么操作，就请返回原数组。
#
#
#
# 示例 1：
#
# 输入：arr = [3,2,1]
# 输出：[3,1,2]
# 解释：交换 2 和 1
# 示例 2：
#
# 输入：arr = [1,1,5]
# 输出：[1,1,5]
# 解释：已经是最小排列
# 示例 3：
#
# 输入：arr = [1,9,4,6,7]
# 输出：[1,7,4,6,9]
# 解释：交换 9 和 7
#
#
# 提示：
#
# 1 <= arr.length <= 104
# 1 <= arr[i] <= 104

from typing import List
from bisect import *

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        stack = []
        i = n - 1
        while i >= 0:
            if len(stack) == 0 or stack[0][0] >= arr[i]:
                stack.insert(0, [arr[i], i])
                i -= 1
            else:
                break
        if i == -1:
            return arr
        pos = bisect_left(stack, arr[i], key=lambda x:x[0]) - 1
        j = stack[pos][1]
        while j - 1 > i and arr[j - 1] == arr[stack[pos][1]]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        return arr


so = Solution()
print(so.prevPermOpt1([3,1,1,3]))
print(so.prevPermOpt1([1,9,4,6,7]))
print(so.prevPermOpt1([3,2,1]))
print(so.prevPermOpt1([1,1,5]))


