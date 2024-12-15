# 给你两个整数数组 arr1 和 arr2，返回使 arr1 严格递增所需要的最小「操作」数（可能为 0）。
#
# 每一步「操作」中，你可以分别从 arr1 和 arr2 中各选出一个索引，分别为 i 和 j，0 <= i < arr1.length 和 0 <= j < arr2.length，然后进行赋值运算 arr1[i] = arr2[j]。
#
# 如果无法让 arr1 严格递增，请返回 -1。
#
#
#
# 示例 1：
#
# 输入：arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
# 输出：1
# 解释：用 2 来替换 5，之后 arr1 = [1, 2, 3, 6, 7]。
# 示例 2：
#
# 输入：arr1 = [1,5,3,6,7], arr2 = [4,3,1]
# 输出：2
# 解释：用 3 来替换 5，然后用 4 来替换 3，得到 arr1 = [1, 3, 4, 6, 7]。
# 示例 3：
#
# 输入：arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
# 输出：-1
# 解释：无法使 arr1 严格递增。
#
#
# 提示：
#
# 1 <= arr1.length, arr2.length <= 2000
# 0 <= arr1[i], arr2[i] <= 10^9
import bisect
from leetcode.allcode.competition.mypackage import *
from collections import Counter
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        n = len(arr1)

        @cache
        def dfs(i, j):  # 前i+1个数，转换为结尾 <j 的最少次数
            if i == -1: return 0
            res = inf
            if arr1[i] < j:
                res = min(res, dfs(i - 1, arr1[i]))
            k = bisect.bisect_left(arr2, j) - 1
            if k >= 0:
                res = min(res, dfs(i - 1, arr2[k]) + 1)
            return res
        ans = dfs(n - 1, inf)
        return ans if ans < inf else -1





obj = Solution()
print(obj.makeArrayIncreasing(distance = [1,2,3,4], start = 0, destination = 1))

