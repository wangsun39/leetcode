from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
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


obj = Solution()
print(obj.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
print(obj.shipWithinDays([3,2,2,4,1,4], 3))

