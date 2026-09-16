# 给你一个整数数组 nums ，以及两个整数 goal 和 k 。
#
# 如果一个 子数组 nums[i..j] 满足其元素和与 goal 之间的 绝对差至少 为 k ，则称其为 遥远的 。
#
# 返回 遥远的 子数组的数量。
#
# 子数组 是数组中连续的非空元素序列。
#
#
#
# 示例 1：
#
# 输入： nums = [1,2,1], goal = 4, k = 1
#
# 输出： 5
#
# 解释：
#
# 对于 k = 1 ，遥远的子数组为：
#
# i	j	nums[i..j]	元素和	abs(sum - goal)
# 0	0	[1]	1	3
# 1	1	[2]	2	2
# 2	2	[1]	1	3
# 0	1	[1, 2]	3	1
# 1	2	[2, 1]	3	1
# 因此，答案为 5。
#
# 示例 2：
#
# 输入： nums = [2,-1,3], goal = 2, k = 2
#
# 输出： 2
#
# 解释：
#
# 对于 k = 2 ，遥远的子数组为：
#
# i	j	nums[i..j]	元素和	abs(sum - goal)
# 1	1	[-1]	-1	3
# 0	2	[2, -1, 3]	4	2
# 因此，答案为 2。
#
# 示例 3：
#
# 输入： nums = [-3,1,2], goal = 0, k = 3
#
# 输出： 2
#
# 解释：
#
# 对于 k = 3 ，遥远的子数组为：
#
# i	j	nums[i..j]	元素和	abs(sum - goal)
# 0	0	[-3]	-3	3
# 1	2	[1, 2]	3	3
# 因此，答案为 2。
#
#
#
# 提示：
#
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# -109 <= goal <= 109
# 0 <= k <= 109

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a


class Fenwick1:
    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def add(self, i: int) -> None:  # + 1
        while i < len(self.tree):
            self.tree[i] += 1
            i += i & -i

    # [1,i] 中的元素和
    def pre(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.tree[i]
            i &= i - 1
        return res

    # [l,r] 中的元素和
    def query(self, l: int, r: int) -> int:
        return self.pre(r) - self.pre(l - 1)


class Solution:
    def distantSubarrays(self, nums: list[int], goal: int, k: int) -> int:
        n = len(nums)
        if k == 0:
            return (n + 1) * n // 2
        s = list(accumulate(nums, initial=0))
        # 查找补集：查找在 goal-k < s[i] - x < goal+k
        # s[i]-goal-k+1<=x<=s[i]-goal+k-1

        # 离散化
        ss = set()
        for t in s:
            ss.add(t)
            ss.add(t-goal-k+1)
            ss.add(t-goal+k-1)
        arr = sorted(list(ss))
        mp = {x: i + 1 for i, x in enumerate(arr)}

        s = [[x, mp[x]] for x in s]
        mx = arr[-1]
        fw = Fenwick1(mp[mx])
        fw.add(s[0][1])
        ans = 0

        for i, [t, mp_t] in enumerate(s[1:], 1):
            lo, hi = mp[t-goal-k+1], mp[t-goal+k-1]
            # print(lo, hi)
            a = fw.query(lo, hi)
            ans += i - a
            fw.add(mp_t)

        return ans



so = Solution()
print(so.distantSubarrays(nums = [2,-1,3], goal = 2, k = 2))
print(so.distantSubarrays(nums = [1,2,1], goal = 4, k = 1))



