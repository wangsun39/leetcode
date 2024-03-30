# 给你一个整数数组 arr 和一个目标值 target ，请你返回一个整数 value ，使得将数组中所有大于 value 的值变成 value 后，数组的和最接近  target （最接近表示两者之差的绝对值最小）。
#
# 如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。
#
# 请注意，答案不一定是 arr 中的数字。
#
#
#
# 示例 1：
#
# 输入：arr = [4,9,3], target = 10
# 输出：3
# 解释：当选择 value 为 3 时，数组会变成 [3, 3, 3]，和为 9 ，这是最接近 target 的方案。
# 示例 2：
#
# 输入：arr = [2,3,5], target = 10
# 输出：5
# 示例 3：
#
# 输入：arr = [60864,25176,27249,21296,20204], target = 56803
# 输出：11361
#
#
# 提示：
#
# 1 <= arr.length <= 10^4
# 1 <= arr[i], target <= 10^5

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        cur = 0
        s = list(accumulate(arr, initial=0))
        mn = inf
        for i in range(arr[-1] + 1):
            while cur < n and arr[cur] <= i:
                cur += 1
            v = s[cur] - s[0] + (n - cur) * i
            if mn != inf and mn <= abs(v - target):
                return i - 1
            if mn > abs(v - target):
                mn = abs(v - target)
        return arr[n - 1]

    def findBestValue(self, arr: List[int], target: int) -> int:
        # 三分法，只适用于严格单调减+严格单调增，或严格单调增+严格单调减，或极值在两端的特殊场景
        # 比如在一个区间内等于恒定值的，不适用
        arr.sort()
        n = len(arr)
        s = list(accumulate(arr, initial=0))
        def calc(val): # 计算value取val时，数组之和
            p = bisect_right(arr, val)
            return s[p] - s[0] + (n - p) * val
        l, r = 0, arr[n - 1]  #
        while l + 1 < r:
            m1 = (l + r) // 2
            if r - l == 2:  # 最后一次循环
                m2 = (l + r) // 2
                if abs(target - calc(l)) < abs(target - calc(r)):
                    r = m2
                else:
                    l = m1
                break
            else:
                # 保证m1 和 m2时不同的
                m2 = m1 + 1
            v1, v2 = abs(target - calc(m1)), abs(target - calc(m2))
            if v1 < v2:
                r = m2
            elif v1 == v2:
                l, r = m1, m2
            else:
                l = m1
        if abs(target - calc(l)) <= abs(target - calc(r)):
            return l
        return r

so = Solution()
print(so.findBestValue(arr = [2,3,5], target = 10))  # 5
print(so.findBestValue(arr = [4,9,3], target = 10))  # 3
print(so.findBestValue(arr = [1547,83230,57084,93444,70879], target = 71237))  # 17422
print(so.findBestValue(arr = [60864,25176,27249,21296,20204], target = 56803))  # 11361




