# 车上最初有 capacity 个空座位。车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向）
#
# 给定整数 capacity 和一个数组 trips ,  trip[i] = [numPassengersi, fromi, toi] 表示第 i 次旅行有 numPassengersi 乘客，接他们和放他们的位置分别是 fromi 和 toi 。这些位置是从汽车的初始位置向东的公里数。
#
# 当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。
#
#
#
# 示例 1：
#
# 输入：trips = [[2,1,5],[3,3,7]], capacity = 4
# 输出：false
# 示例 2：
#
# 输入：trips = [[2,1,5],[3,3,7]], capacity = 5
# 输出：true
#
#
# 提示：
#
# 1 <= trips.length <= 1000
# trips[i].length == 3
# 1 <= numPassengersi <= 100
# 0 <= fromi < toi <= 1000
# 1 <= capacity <= 105

from leetcode.allcode.competition.mypackage import *

class MountainArray:
    def __init__(self, arr):
        self.m = arr[:]
    def get(self, index: int) -> int:
        return self.m[index]
    def length(self) -> int:
        return len(self.m)

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        if n == 0: return -1
        if mountainArr.get(0) == target: return 0
        if n == 1: return  -1
        if mountainArr.get(1) == target: return 1
        if n == 2: return -1
        if mountainArr.get(0) > target and mountainArr.get(n - 1) > target: return -1
        lo, hi = 0, n - 1
        while lo < hi - 1:
            mid = (lo + hi) // 2
            if mountainArr.get(mid - 1) < mountainArr.get(mid) > mountainArr.get(mid + 1):
                peak = mid
                break
            if mountainArr.get(mid - 1) < mountainArr.get(mid) < mountainArr.get(mid + 1):
                lo = mid
            else:
                hi = mid
        if mountainArr.get(peak) < target: return -1
        if mountainArr.get(peak) == target: return peak
        if mountainArr.get(0) < target:
            lo, hi = 0, peak
            while lo < hi - 1:
                mid = (lo + hi) // 2
                v = mountainArr.get(mid)
                if v == target: return mid
                if v > target: hi = mid
                else: lo = mid
        if mountainArr.get(n-1) == target: return n - 1
        if mountainArr.get(n - 1) < target:
            lo, hi = peak, n - 1
            while lo < hi - 1:
                mid = (lo + hi) // 2
                v = mountainArr.get(mid)
                if v == target: return mid
                if v > target:
                    lo = mid
                else:
                    hi = mid
        return -1


ma = MountainArray([1,2,3,5,3])

obj = Solution()
print(obj.findInMountainArray(3, ma))

