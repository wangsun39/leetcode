# 给你一个长度为 n 的整数数组 nums。
#
# 对于每个 正整数 g，定义 g 的 美丽值 为 g 与 nums 中符合要求的子序列数量的乘积，子序列需要 严格递增 且最大公约数（GCD）恰好为 g 。
#
# 请返回所有正整数 g 的 美丽值 之和。
#
# 由于答案可能非常大，请返回结果对 109 + 7 取模后的值。
#
# 子序列 是一个 非空 数组，可以通过从另一个数组中删除某些元素（或不删除任何元素）而保持剩余元素顺序不变得到。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3]
#
# 输出：10
#
# 解释：
#
# 所有严格递增子序列及其 GCD 如下：
#
# 子序列	GCD
# [1]	1
# [2]	2
# [3]	3
# [1,2]	1
# [1,3]	1
# [2,3]	1
# [1,2,3]	1
# 计算每个 GCD 的美丽值：
#
# GCD	子序列数量	美丽值 (GCD × 数量)
# 1	5	1 × 5 = 5
# 2	1	2 × 1 = 2
# 3	1	3 × 1 = 3
# 美丽值总和为 5 + 2 + 3 = 10。
#
# 示例 2：
#
# 输入：nums = [4,6]
#
# 输出：12
#
# 解释：
#
# 所有严格递增子序列及其 GCD 如下：
#
# 子序列	GCD
# [4]	4
# [6]	6
# [4,6]	2
# 计算每个 GCD 的美丽值：
#
# GCD	子序列数量	美丽值 (GCD × 数量)
# 2	1	2 × 1 = 2
# 4	1	4 × 1 = 4
# 6	1	6 × 1 = 6
# 美丽值总和为 2 + 4 + 6 = 12。
#
#
#
# 提示：
#
# 1 <= n == nums.length <= 104
# 1 <= nums[i] <= 7 × 104

from leetcode.allcode.competition.mypackage import *

MX = 7 * 10 ** 4 + 1
divisors = [[] for _ in range(MX)]  # divisors[i] 表示 i 的所有因子
for i in range(1, MX):  # 预处理每个数的所有因子，时间复杂度 O(MlogM)，M=1e5
    for j in range(i, MX, i):
        divisors[j].append(i)

MOD = 10 ** 9 + 7

now = 0
class Fenwick:
    # 所有函数参数下标从1开始，可以传入使用者的数值x+1的值
    __slots__ = ['f', 'nums', 'time']

    def __init__(self, n: int):
        # n 是能调用下面函数的下标最大值
        self.f = [0] * (n + 1)  # 关键区间
        self.nums = [0] * (n + 1)
        self.time = [0] * (n + 1)

    def add(self, i: int, val: int) -> None:  # nums[i] += val
        global now
        self.nums[i] += val
        while i < len(self.f):
            if self.time[i] < now:
                self.f[i] = 0  # 懒更新
                self.time[i] = now
            self.f[i] += val
            i += i & -i

    def pre(self, i: int) -> int:  # 下标<=i的和
        res = 0
        while i > 0:
            if self.time[i] == now:
                res += self.f[i]
            i &= i - 1
        return res


class Solution:
    def totalBeauty(self, nums: List[int]) -> int:
        global now
        mx = max(nums)
        group = defaultdict(list)  # group[x] 表示包含因子x的，所有nums中的数字
        for x in nums:
            for y in divisors[x]:
                group[y].append(x)

        fw = Fenwick(mx)  # 记录前缀和
        counter = {}  # counter[x] 表示以x为公因子，且单调增的子序列数量
        ans = 0
        for g in range(mx, 0, -1):  # 从mx开始，枚举 g 确定以g为因子的数都在 group[y] 中
            # 要找到所有group[y]的单调升的子序列数量
            # 使用懒更新的树状树状，防止多次初始化
            s = 0  # 记录这样的子序列数量，即以g或g的整数倍为公因子的子序列数量
            for x in group[g]:
                v = fw.pre(x - 1) + 1
                s += v
                s %= MOD
                fw.add(x, v)
            i = 2
            while i * g <= mx:
                s -= counter[i * g]   # 容斥原理，减去是g整数倍的子
                i += 1
            counter[g] = s % MOD
            ans += counter[g] * g
            ans %= MOD
            now += 1

        return ans





so = Solution()
print(so.totalBeauty(nums = [1,2,3]))




