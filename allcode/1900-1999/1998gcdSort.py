# 给你一个整数数组 nums ，你可以在 nums 上执行下述操作 任意次 ：
#
# 如果 gcd(nums[i], nums[j]) > 1 ，交换 nums[i] 和 nums[j] 的位置。其中 gcd(nums[i], nums[j]) 是 nums[i] 和 nums[j] 的最大公因数。
# 如果能使用上述交换方式将 nums 按 非递减顺序 排列，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入：nums = [7,21,3]
# 输出：true
# 解释：可以执行下述操作完成对 [7,21,3] 的排序：
# - 交换 7 和 21 因为 gcd(7,21) = 7 。nums = [21,7,3]
# - 交换 21 和 3 因为 gcd(21,3) = 3 。nums = [3,7,21]
# 示例 2：
#
# 输入：nums = [5,2,6,2]
# 输出：false
# 解释：无法完成排序，因为 5 不能与其他元素交换。
# 示例 3：
#
# 输入：nums = [10,5,9,3,15]
# 输出：true
# 解释：
# 可以执行下述操作完成对 [10,5,9,3,15] 的排序：
# - 交换 10 和 15 因为 gcd(10,15) = 5 。nums = [15,5,9,3,10]
# - 交换 15 和 3 因为 gcd(15,3) = 3 。nums = [3,5,9,15,10]
# - 交换 10 和 15 因为 gcd(10,15) = 5 。nums = [3,5,9,10,15]
#
#
# 提示：
#
# 1 <= nums.length <= 3 * 104
# 2 <= nums[i] <= 105

from leetcode.allcode.competition.mypackage import *

MX = 10 ** 5 + 1
# MX = 10
omega = [[] for _ in range(MX)]  # omega[i]  表示i的质因子个数
for i in range(2, MX):  # 预处理 omega
    if len(omega[i]) == 0:  # i 是质数
        for j in range(i, MX, i):
            omega[j].append(i)  # i 是 j 的一个质因子
# print(omega)

class UnionFind:
    def __init__(self, n):
        self.fa = list(range(n))
    def find(self, x):
        if x != self.fa[x]:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        self.fa[self.find(y)] = self.find(x)

    def getSon(self):
        son = defaultdict(list)
        for i, x in enumerate(self.fa):
            son[x].append(i)
        return son

class Solution:
    def gcdSort1(self, nums: List[int]) -> bool:
        n = len(nums)
        x_to_i = defaultdict(list)
        for i, x in enumerate(nums):
            x_to_i[x].append(i)
        fa1 = UnionFind(max(nums) + 1)

        for x in nums:
            for y in omega[x]:
                fa1.union(x, y)  # 保证代表元是x
        for x in nums:
            fa1.find(x)

        rep = defaultdict(list)  # 代表元下的所有元素
        for x in nums:
            rep[fa1.find(x)].append(x)

        for x in rep:
            rep[x].sort()  # 组内排序

        ans = [0] * n
        for i in range(n):
            ans[i] = rep[fa1.find(nums[i])].pop(0)
            if i and ans[i] < ans[i - 1]: return False
        return True


    def gcdSort(self, nums: List[int]) -> bool:
        # 不需要组内排序的方法
        n = len(nums)
        x_to_i = defaultdict(list)
        for i, x in enumerate(nums):
            x_to_i[x].append(i)
        fa1 = UnionFind(max(nums) + 1)

        for x in nums:
            for y in omega[x]:
                fa1.union(x, y)  # 保证代表元是x
        for x in nums:
            fa1.find(x)

        ans = nums[:]
        ans.sort()
        if any(fa1.find(ans[i]) != fa1.find(nums[i]) for i in range(n)):
            return False
        return True


so = Solution()
print(so.gcdSort(nums = [7,21,3]))  # True
print(so.gcdSort(nums = [5,2,6,2]))  # False


