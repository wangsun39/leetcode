# 给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。
#
# 请你找到并返回这个整数
#
#
#
# 示例：
#
# 输入：arr = [1,2,2,6,6,6,6,7,10]
# 输出：6
#
#
# 提示：
#
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^5

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        delta = n // 4 + 1
        cand = []
        for i in range(0, n, delta):
            cand.append(arr[i])
            p1 = bisect_left(arr, arr[i])
            p2 = bisect_right(arr, arr[i])
            if (p2 - p1) * 4 > n:
                return arr[i]

obj = Solution()
print(obj.findSpecialInteger( [[0],[1],[1]]))
