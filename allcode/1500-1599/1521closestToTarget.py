# Winston 构造了一个如上所示的函数 func 。他有一个整数数组 arr 和一个整数 target ，他想找到让 |func(arr, l, r) - target| 最小的 l 和 r 。
#
# 请你返回 |func(arr, l, r) - target| 的最小值。
#
# 请注意， func 的输入参数 l 和 r 需要满足 0 <= l, r < arr.length 。
#
#
#
# 示例 1：
#
# 输入：arr = [9,12,3,7,15], target = 5
# 输出：2
# 解释：所有可能的 [l,r] 数对包括 [[0,0],[1,1],[2,2],[3,3],[4,4],[0,1],[1,2],[2,3],[3,4],[0,2],[1,3],[2,4],[0,3],[1,4],[0,4]]， Winston 得到的相应结果为 [9,12,3,7,15,8,0,3,7,0,0,3,0,0,0] 。最接近 5 的值是 7 和 3，所以最小差值为 2 。
# 示例 2：
#
# 输入：arr = [1000000,1000000,1000000], target = 1
# 输出：999999
# 解释：Winston 输入函数的所有可能 [l,r] 数对得到的函数值都为 1000000 ，所以最小差值为 999999 。
# 示例 3：
#
# 输入：arr = [1,2,4,8,16], target = 0
# 输出：0
#
#
# 提示：
#
# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 10^6
# 0 <= target <= 10^7

from leetcode.allcode.competition.mypackage import *

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        n = len(arr)
        counter = Counter()
        def bits(x):  # 把一个数字转成各个bit的计数
            res = Counter()
            for i in range(32):
                if x == 0: return res
                if x & 1: res[i] = 1
                x >>= 1
            return res
        def calc(counter, l):  # 根据counter和区间长度，计算 and 的值
            res = 0
            for k, v in counter.items():
                if v == l:
                    res |= (1 << k)
            return res

        ans = inf
        l = 0
        for r in range(n):
            if arr[r] == target:
                return 0
            if arr[r] < target:  # 处理区间 [l, r - 1]，不断右移l
                ans = min(ans, target - arr[r])
                while l <= r - 1:
                    counter -= bits(arr[l])
                    s = calc(counter, r - l)
                    ans = min(ans, abs(s - target))
                    l += 1
                l = r + 1
                counter = Counter()
                continue
            counter += bits(arr[r])
            s = calc(counter, r - l + 1)
            if s >= target:
                ans = min(ans, s - target)
                if ans == 0: return 0
                continue
            ans = min(ans, target - s)
            while s <= target:
                counter -= bits(arr[l])
                s = calc(counter, r - l)
                ans = min(ans, abs(s - target))
                if ans == 0: return 0
                l += 1

        return ans




so = Solution()
print(so.closestToTarget([2,70,41,63,60,55,51,85,60,77,56,24,66,13,91,28,31,92,79,85], 33))  # 1
print(so.closestToTarget([10,15,7], 2))  # 0
print(so.closestToTarget([10,9,11,22,32], 4))  # 2
print(so.closestToTarget([4095,31,262143,8191,63,2047,31,63,4095,131071,524287,32767], 33))  # 2
print(so.closestToTarget(arr = [9,12,3,7,15], target = 5))
print(so.closestToTarget(arr = [1000000,1000000,1000000], target = 1))   # 999999
print(so.closestToTarget(arr = [1,2,4,8,16], target = 0))
print(so.closestToTarget([59,63,31,53],21))
print(so.closestToTarget([6,5,1], 1))
print(so.closestToTarget([5,89,79,44,45,79], 965))   # 876




