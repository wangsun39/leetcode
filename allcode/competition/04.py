

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        ones = [i for i, x in enumerate(nums) if x == 1]
        s = list(accumulate(ones, initial=0))
        left = SortedList()
        right = SortedList()
        n = len(nums)
        if n > 3:
            right = SortedList(i for i in range(3, n) if nums[i] == 1)

        def get(p, v):  # 计算以p为index，使用方法二的动作，最多的动作次数
            lo, hi = 1, 10 ** 5 + 1
            while lo < hi - 1:
                mid = (lo + hi) // 2
                pl = left.bisect_right(-p - mid)
                pr = right.bisect_right(p + mid)
                if pl + pr >= v:
                    hi = mid
                else:
                    lo = mid
            # hi 是向两侧最远的需要交换的距离
            pl = left.bisect_right(-p - hi)
            pr = right.bisect_right(p + hi)
            if pl + pr == v:
                idl = -left[pl] if pl < len(left) else 0
                idr = right[pr] if pr < len(right) else n - 1
                lact = s[p - 2] - s[idl]
                ract = s[idr + 1] - s[p + 3]
                return lact + ract
            lact = s[p] - s[-left[pl]]
            ract = s[p + pr - 1] - s[p]
            return lact + ract
        def calc(p):
            act = got = 0  # got是拾到1的个数，act是行动次数
            if nums[p] == 1:
                got = 1
            if got >= k: return act
            if p > 0 and nums[p - 1] == 1:
                act += 1
                got += 1
            if got >= k: return act
            if p < n - 1 and nums[p + 1] == 1:
                act += 1
                got += 1
            if got >= k: return act
            if p > 1 and nums[p - 2] == 1:
                act += 2
                got += 1
            if got >= k: return act
            if p < n - 2 and nums[p + 2] == 1:
                act += 2
                got += 1
            if got >= k: return act
            if got + maxChanges >= k:
                return got + (k - got) * 2
            act += maxChanges * 2
            got += maxChanges
            return act + get(p, k - got)

        ans = inf
        for pos in range(n):  # 枚举index位置
            if pos > 0:
                if right and right[0] <= pos + 2:
                    right.pop(0)
                if pos - 3 >= 0 and nums[pos - 3] == 1:
                    left.add(-(pos - 3))
            ans = min(ans, calc(pos))
        return ans


so = Solution()
print(so.minimumMoves(nums = [1,1,0,0,0,1,1,0,0,1], k = 3, maxChanges = 1))




