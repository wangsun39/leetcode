# n 名士兵站成一排。每个士兵都有一个 独一无二 的评分 rating 。
#
# 从中选出 3 个士兵组成一个作战单位，规则如下：
#
# 从队伍中选出下标分别为 i、j、k 的 3 名士兵，他们的评分分别为 rating[i]、rating[j]、rating[k]
# 作战单位需满足： rating[i] < rating[j] < rating[k] 或者 rating[i] > rating[j] > rating[k] ，其中  0 <= i < j < k < n
# 请你返回按上述条件组建的作战单位的方案数。
#
#
#
# 示例 1：
#
# 输入：rating = [2,5,3,4,1]
# 输出：3
# 解释：我们可以组建三个作战单位 (2,3,4)、(5,4,1)、(5,3,1) 。
# 示例 2：
#
# 输入：rating = [2,1,3]
# 输出：0
# 解释：根据题目条件，我们无法组建作战单位。
# 示例 3：
#
# 输入：rating = [1,2,3,4]
# 输出：4
#
#
# 提示：
#
# n == rating.length
# 3 <= n <= 1000
# 1 <= rating[i] <= 10^5
# rating 中的元素都是唯一的

from leetcode.allcode.competition.mypackage import *

class Fenwick:
    # 所有函数参数下标从1开始，可以传入使用者的数值x+1的值
    __slots__ = ['f', 'nums']

    def __init__(self, n: int):
        # n 是能调用下面函数的下标最大值
        self.f = [0] * (n + 1)  # 关键区间
        self.nums = [0] * (n + 1)

    def add(self, i: int, val: int) -> None:  # nums[i] += val
        self.nums[i] += val
        while i < len(self.f):
            self.f[i] += val
            i += i & -i

    def update(self, i: int, val: int) -> None:  # nums[i] += val
        delta = val - self.nums[i]
        self.add(i, delta)

    def pre(self, i: int) -> int:  # 下标<=i的和
        res = 0
        while i > 0:
            res += self.f[i]
            i &= i - 1
        return res

    def query_one(self, idx: int):
        return self.nums[idx]

    def query(self, l: int, r: int) -> int:  # [l, r]  区间求和
        if r < l:
            return 0
        return self.pre(r) - self.pre(l - 1)

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        mx = max(rating)
        n = len(rating)
        left1 = [0] * n  # nums[i] 左边有多少个比它小的数
        left2 = [0] * n  # nums[i] 左边有多少个比它大的数
        right1 = [0] * n  # nums[i] 右边有多少个比它小的数
        right2 = [0] * n  # nums[i] 右边有多少个比它大的数
        fw = Fenwick(mx + 1)
        for i, x in enumerate(rating):
            left1[i] = fw.pre(x)  # <= x 的元素个数
            left2[i] = fw.query(x + 2, mx + 1)  # >= x + 2 的元素个数, x的个数 记录在 x + 1 上
            fw.add(x + 1, 1)  # x的个数 记录在 x + 1 上

        fw = Fenwick(mx + 1)
        for i in range(n - 1, -1, -1):
            x = rating[i]
            right1[i] = fw.pre(x)  # <= x 的元素个数
            right2[i] = fw.query(x + 2, mx + 1)  # >= x + 2 的元素个数, x的个数 记录在 x + 1 上
            fw.add(x + 1, 1)  # x的个数 记录在 x + 1 上

        ans = 0
        for i in range(1, n - 1):
            ans += left1[i] * right2[i]
            ans += left2[i] * right1[i]
        return ans

so = Solution()
print(so.numTeams(rating = [3,7,5,6]))
print(so.numTeams(rating = [2,5,3,4,1]))
print(so.numTeams(rating = [2,1,3]))




