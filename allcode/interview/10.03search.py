# 搜索旋转数组。给定一个排序后的数组，包含n个整数，但这个数组已被旋转过很多次了，次数不详。请编写代码找出数组中的某个元素，假设数组元素原先是按升序排列的。若有多个相同元素，返回索引值最小的一个。
#
# 示例 1：
#
#  输入：arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 5
#  输出：8（元素5在该数组中的索引）
# 示例 2：
#
#  输入：arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 11
#  输出：-1 （没有找到）
# 提示:
#
# arr 长度范围在[1, 1000000]之间

from leetcode.allcode.competition.mypackage import *

class Solution:
    def search(self, arr: List[int], target: int) -> int:
        if target == arr[0]: return 0
        n = len(arr)
        mx = None
        def dfs(left, right):
            nonlocal mx
            if left >= right: return
            if left + 1 == right:
                if arr[left] > arr[right]:
                    mx = left
                    return True
            else:
                mid = (left + right) // 2
                if arr[left] < arr[mid]:
                    dfs(mid, right)
                elif arr[left] > arr[mid]:
                    dfs(left, mid)
                else:
                    return dfs(left, mid) or dfs(mid, right)
        dfs(0, n - 1)
        if mx is None:
            return -1
        arr1, arr2 = arr[: mx + 1], arr[mx + 1:]
        len1, len2 = len(arr1), len(arr2)
        if target > arr[0]:
            p = bisect_left(arr, target, 0, mx + 1)
            if p > mx or arr[p] != target:
                return -1
            return p
        else:
            p = bisect_left(arr, target, mx + 1, n)
            if p > n - 1 or arr[p] != target:
                return -1
            return p




so = Solution()
print(so.search(arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 5))




