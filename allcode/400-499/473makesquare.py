# 还记得童话《卖火柴的小女孩》吗？现在，你知道小女孩有多少根火柴，请找出一种能使用所有火柴拼成一个正方形的方法。不能折断火柴，可以把火柴连接起来，并且每根火柴都要用到。
#
# 输入为小女孩拥有火柴的数目，每根火柴用其长度表示。输出即为是否能用所有的火柴拼成正方形。
#
# 示例1:
#
# 输入: [1,1,2,2,2]
# 输出: true
#
# 解释: 能拼成一个边长为2的正方形，每边两根火柴。
# 示例2:
#
# 输入: [3,3,3,3,4]
# 输出: false
#
# 解释: 不能用所有火柴拼成一个正方形。
# 注意:
#
# 给定的火柴长度和在0到10^9之间。
# 火柴数组的长度不超过15。

import time


from typing import List
import copy
from functools import lru_cache
class Solution:
    def makesquare2(self, matchsticks: List[int]) -> bool:
        start = time.time()
        sumAll = sum(matchsticks)
        if sumAll % 4 != 0:
            return False
        sumEdge = sumAll // 4
        print(sumEdge)
        groups = []  # 按长度分组，统计各组个数，并排序
        for m in matchsticks:
            exist = False
            for e in groups:
                if e[0] == m:
                    e[1] += 1
                    exist = True
                    break
            if not exist:
                groups.append([m, 1])
        groups = sorted(groups, key=lambda x: x[0])
        print(groups)

        def f(groups, expect):  # 返回 和为 expect 的各种组合,没有重复
            if expect == 0 or len(groups) == 0:
                return []
            z = []
            x = []
            # 仅考虑 groups[0] 元素，可以取0个，1个。。。 直到所以这个相同元素或和超过expect
            # 对于 groups[1:] 的元素，就依靠递归完成，这样可以避免递归
            for j in range(groups[0][1] + 1):
                diff = expect - groups[0][0] * j
                if diff < 0:
                    break
                if j > 0:
                    x.append(groups[0][0])
                if diff == 0:
                    z.append(x)
                    break
                y = f(groups[1:], diff)
                for yy in y:
                    z.append(x + yy)
            return z
        # print('xxx=', f([[1, 1], [2, 1]], 2))
        # g1 是按元素分组并排序的结构，用它减去已选用的数，获得剩余元素的分组排序结构
        def minus(g1, s2):
            i, j = 0, 0
            g3 = copy.deepcopy(g1)
            while True:
                if g3[i][0] == s2[j]:
                    g3[i][1] -= 1
                    j += 1
                    if j == len(s2):
                        break
                else:
                    i += 1
            return g3

        A1 = f(groups, sumEdge)
        if len(A1) == 0:
            return False
        print(len(A1), 'A1:', A1)

        for a1 in A1:
            remain = minus(groups, a1)
            A2 = f(remain, sumEdge)
            # print(a1)
            if len(A2) == 0:
                continue
            print('a1:', a1, 'A2:', A2)
            for a2 in A2:
                remain1 = minus(remain, a2)
                A3 = f(remain1, sumEdge)
                if len(A3) == 0:
                    continue
                now = time.time()
                print('time = ', now - start)
                return True
        return False

    def makesquare1(self, nums):  # 官方的解法
        """
        :type nums: List[int]
        :rtype: bool
        """

        # If there are no matchsticks, then we can't form any square.
        start = time.time()
        if not nums:
            return False

        # Number of matchsticks
        L = len(nums)

        # Possible perimeter of our square
        perimeter = sum(nums)

        # Possible side of our square from the given matchsticks
        possible_side = perimeter // 4

        # If the perimeter isn't equally divisible among 4 sides, return False.
        if possible_side * 4 != perimeter:
            return False

        # Memoization cache for the dynamic programming solution.
        memo = {}

        # mask and the sides_done define the state of our recursion.
        def recurse(mask, sides_done):

            # This will calculate the total sum of matchsticks used till now using the bits of the mask.
            total = 0
            for i in range(L - 1, -1, -1):
                if not (mask & (1 << i)):
                    total += nums[L - 1 - i]

            # If some of the matchsticks have been used and the sum is divisible by our square's side, then we increment the number of sides completed.
            if total > 0 and total % possible_side == 0:
                sides_done += 1

            # If we were successfully able to form 3 sides, return True
            if sides_done == 3:
                return True

            # If this recursion state has already been calculated, just return the stored value.
            if (mask, sides_done) in memo:
                return memo[(mask, sides_done)]

            # Common variable to store answer from all possible further recursions from this step.
            ans = False

            # rem stores available space in the current side (incomplete).
            c = int(total / possible_side)
            rem = possible_side * (c + 1) - total

            # Iterate over all the matchsticks
            for i in range(L - 1, -1, -1):

                # If the current one can fit in the remaining space of the side and it hasn't already been taken, then try it out
                if nums[L - 1 - i] <= rem and mask & (1 << i):

                    # If the recursion after considering this matchstick gives a True result, just break. No need to look any further.
                    # mask ^ (1 << i) makes the i^th from the right, 0 making it unavailable in future recursions.
                    if recurse(mask ^ (1 << i), sides_done):
                        ans = True
                        break
            # cache the result for the current recursion state.
            memo[(mask, sides_done)] = ans
            return ans

        # recurse with the initial mask with all matchsticks available.
        ret = recurse((1 << L) - 1, 0)
        now = time.time()
        print('time = ', now - start)
        return ret

    # 2022.6.4 个人解法
    def makesquare(self, matchsticks: List[int]) -> bool:
        total, n = sum(matchsticks), len(matchsticks)
        if total % 4 != 0 or n < 4:
            return False
        edge = total // 4
        matchsticks.sort()
        if matchsticks[-1] > edge:
            return False
        idle = int(2 ** n) - 1
        print(idle)

        @lru_cache(None)
        def helper(idle, target):
            if target == 0:
                if idle == 0:
                    return True
                else:
                    return helper(idle, edge)
            for i in range(n):
                if idle & (1 << i):
                    if matchsticks[i] > target:
                        return False
                    res = helper(idle & ~(1 << i), target - matchsticks[i])
                    if res:
                        return True
            return False
        return helper(idle, edge)

so = Solution()

print(so.makesquare([5,5,5,5,4,4,4,4,3,3,3,3]))
print(so.makesquare([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(so.makesquare([1,1,2,2,2]))
print(so.makesquare([3,3,3,3,4]))


