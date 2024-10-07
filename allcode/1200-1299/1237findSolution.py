
# 你打算利用空闲时间来做兼职工作赚些零花钱。
#
# 这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。
#
# 给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。
#
# 注意，时间上出现重叠的 2 份工作不能同时进行。
#
# 如果你选择的工作在时间 X 结束，那么你可以立刻进行在时间 X 开始的下一份工作。
#
#
#
# 示例 1：
#
#
#
# 输入：startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# 输出：120
# 解释：
# 我们选出第 1 份和第 4 份工作，
# 时间范围是 [1-3]+[3-6]，共获得报酬 120 = 50 + 70。
# 示例 2：
#
#
#
# 输入：startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
# 输出：150
# 解释：
# 我们选择第 1，4，5 份工作。
# 共获得报酬 150 = 20 + 70 + 60。
# 示例 3：
#
#
#
# 输入：startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
# 输出：6
#
#
# 提示：
#
# 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
# 1 <= startTime[i] < endTime[i] <= 10^9
# 1 <= profit[i] <= 10^4

# https://leetcode.cn/problems/maximum-profit-in-job-scheduling/

from leetcode.allcode.competition.mypackage import *

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""

from bisect import *

class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        return x + y

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        for x in range(1, 1001):
            lo, hi = 1, 1001
            v1 = customfunction.f(x, lo)
            if v1 > z: continue
            if v1 == z:
                ans.append([x, lo])
                continue
            v2 = customfunction.f(x, hi)
            if v2 < z: continue
            if v2 == z:
                ans.append([x, hi])
                continue

            while lo < hi - 1:
                mid = (lo + hi) // 2
                v = customfunction.f(x, mid)
                if v == z:
                    ans.append([x, mid])
                    break
                if v > z:
                    hi = mid
                else:
                    lo = mid

        return ans


cf = CustomFunction()
obj = Solution()
print(obj.findSolution(cf, 5))  #

