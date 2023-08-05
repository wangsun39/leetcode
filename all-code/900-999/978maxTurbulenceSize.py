# 给定一个整数数组 arr ，返回 arr 的 最大湍流子数组的长度 。
#
# 如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是 湍流子数组 。
#
# 更正式地来说，当 arr 的子数组 A[i], A[i+1], ..., A[j] 满足仅满足下列条件时，我们称其为湍流子数组：
#
# 若 i <= k < j ：
# 当 k 为奇数时， A[k] > A[k+1]，且
# 当 k 为偶数时，A[k] < A[k+1]；
# 或 若 i <= k < j ：
# 当 k 为偶数时，A[k] > A[k+1] ，且
# 当 k 为奇数时， A[k] < A[k+1]。
#
#
# 示例 1：
#
# 输入：arr = [9,4,2,10,7,8,8,1,9]
# 输出：5
# 解释：arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
# 示例 2：
#
# 输入：arr = [4,8,12,16]
# 输出：2
# 示例 3：
#
# 输入：arr = [100]
# 输出：1
#
#
# 提示：
#
# 1 <= arr.length <= 4 * 104
# 0 <= arr[i] <= 109

from math import log
from typing import List
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = 1
        sign = 0  # 1 表示当前数大于前一个数，-1 相反
        cur = 0
        for i, x in enumerate(arr[1:], 1):
            if x > arr[i - 1]:
                if sign == -1:
                    cur += 1
                else:
                    cur = 2
                sign = 1
            elif x == arr[i - 1]:
                sign = 0
                cur = 0
            else:
                if sign == 1:
                    cur += 1
                else:
                    cur = 2
                sign = -1
            ans = max(ans, cur)
        return ans

so = Solution()
print(so.maxTurbulenceSize(arr = [4,8,12,16]))
print(so.maxTurbulenceSize(arr = [9,4,2,10,7,8,8,1,9]))
print(so.maxTurbulenceSize(arr = [100]))

