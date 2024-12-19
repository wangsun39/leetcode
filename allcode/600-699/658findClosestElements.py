# 给定一个 排序好 的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。
#
# 整数 a 比整数 b 更接近 x 需要满足：
#
# |a - x| < |b - x| 或者
# |a - x| == |b - x| 且 a < b
#  
#
# 示例 1：
#
# 输入：arr = [1,2,3,4,5], k = 4, x = 3
# 输出：[1,2,3,4]
# 示例 2：
#
# 输入：arr = [1,2,3,4,5], k = 4, x = -1
# 输出：[1,2,3,4]
#  
#
# 提示：
#
# 1 <= k <= arr.length
# 1 <= arr.length <= 104
# arr 按 升序 排列
# -104 <= arr[i], x <= 104



# 注意: 二叉树的高度在范围 [1, 10] 中。
from leetcode.allcode.competition.mypackage import *

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pos = bisect.bisect_left(arr, x)
        p1, p2 = pos - 1, pos
        ans = []
        while len(ans) < k:
            if p1 < 0:
                ans.append(arr[p2])
                p2 += 1
            elif p2 >= len(arr):
                ans.insert(0, arr[p1])
                p1 -= 1
            else:
                if abs(arr[p1] - x) <= abs(arr[p2] - x):
                    ans.insert(0, arr[p1])
                    p1 -= 1
                else:
                    ans.append(arr[p2])
                    p2 += 1
        return ans

so = Solution()
print(so.findClosestElements(arr = [0,0,1,2,3,3,4,7,7,8], k = 3, x = 5))
print(so.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3))
print(so.findClosestElements(arr = [1,2,3,4,5], k = 4, x = -1))

