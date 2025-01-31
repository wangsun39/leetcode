# 给定一个长度为 n 的整数 山脉 数组 arr ，其中的值递增到一个 峰值元素 然后递减。
#
# 返回峰值元素的下标。
#
# 你必须设计并实现时间复杂度为 O(log(n)) 的解决方案。
#
#
#
# 示例 1：
#
# 输入：arr = [0,1,0]
# 输出：1
# 示例 2：
#
# 输入：arr = [0,2,1,0]
# 输出：1
# 示例 3：
#
# 输入：arr = [0,10,5,2]
# 输出：1
#
#
# 提示：
#
# 3 <= arr.length <= 105
# 0 <= arr[i] <= 106
# 题目数据 保证 arr 是一个山脉数组

from leetcode.allcode.competition.mypackage import *

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 0, n - 1
        while l + 2 < r:
            m1, m2 = (2 * l + r) // 3, (l + 2 * r) // 3
            if arr[m1] == arr[m2]:
                l = m1
                r = m2
            elif arr[l] < arr[m1] > arr[m2]:
                r = m2
            elif arr[m1] < arr[m2] > arr[r]:
                l = m1
            elif arr[l] < arr[m1] < arr[m2]:
                l = m1
            elif arr[m1] > arr[m2] > arr[r]:
                r = m2

        return l + 1



so = Solution()
print(so.peakIndexInMountainArray([12,13,19,41,55,69,70,71,96,72]))
print(so.peakIndexInMountainArray([0,2,1,0]))
print(so.peakIndexInMountainArray([0,1,0]))


