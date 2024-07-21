

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        diff = [target[i] - nums[i] for i in range(n)]
        group = []  # 把 nums 分成多个组，每组都是的差值符号是相同的
        start = 0
        for i, x in enumerate(diff):
            if x == 0: continue
            if x > 0:
                if diff[start] == 0:
                    start = i
                elif diff[start] < 0:
                    group.append([start, i])
                    start = i
            else:
                if diff[start] == 0:
                    start = i
                elif diff[start] > 0:
                    group.append([start, i])
                    start = i
        group.append([start, n])

        def calc(l):
            if any(x < 0 for x in l):
                l = [-x for x in l]
            l.insert(0, 0)
            ans = 0
            for i, x in enumerate(l[1:], 1):
                if x >= l[i - 1]:
                    ans += x - l[i - 1]
                    continue
            return ans

        return sum(calc(diff[x: y]) for x, y in group)



so = Solution()
print(so.minimumOperations(nums = [3,5,1,2], target = [4,6,2,4]))
print(so.minimumOperations(nums = [1,3,2], target = [2,1,4]))




