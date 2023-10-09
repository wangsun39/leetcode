from typing import List
class Solution:
    def shipWithinDays1(self, weights: List[int], D: int) -> int:
        maxW, sumW = max(weights), sum(weights)
        res = max(maxW, int((sumW+D-1) / D))
        def DaysNumWithinCapacity(cap):
            curCap = 0
            days = 1
            for w in weights:
                curCap += w
                if curCap > cap:
                    days += 1
                    if days > D:
                        return days
                    curCap = w
            return days
        while True:
            days = DaysNumWithinCapacity(res)
            if days <= D:
                return res
            res += 1

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # 2023/6/5
        def check(cap):
            cnt = 0
            d = 0
            for i, x in enumerate(weights):
                if cnt + x <= cap:
                    cnt += x
                else:
                    d += 1
                    cnt = x
                if i == len(weights) - 1:
                    d += 1
            if d <= days:
                return True
            return False
        lo, hi = max(weights) - 1, sum(weights)  # max(weights) - 1 是一定满足不了的
        while lo < hi - 1:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid
        return hi


obj = Solution()
print(obj.shipWithinDays([1,2,3,1,1], 4))
print(obj.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
print(obj.shipWithinDays([3,2,2,4,1,4], 3))

