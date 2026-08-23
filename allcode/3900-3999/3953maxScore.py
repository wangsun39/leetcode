# 给你一个长度为 n 的整数数组 nums 和一个整数 maxVal。
#
# 你 可以 将 nums 中的任意元素更改为 小于或等于 maxVal 的任意正整数。每次这样的更改代价为 1。
#
# 如果两个整数的 最大公约数（GCD） 为 1，则这两个整数 互质。
#
# 在所有修改之后，你 必须 选择一个下标 i，使得 nums[i] 与所有其他元素 nums[j] 互质。
#
# 令：
#
# selectedValue 为修改后 nums[i] 的最终值。
# modificationCost 为更改的元素总数。
# 得分定义为 score = selectedValue - modificationCost
#
# 返回 最大 可能得分。
#
# gcd(a, b) 表示 a 和 b 的 最大公约数。
#
#
# 示例 1：
#
# 输入： nums = [3,4,6], maxVal = 5
#
# 输出： 4
#
# 解释：
#
# 将 nums[2] 从 6 更改为 5，代价为 1。选择 nums[2] = 5，因为它与 3 和 4 互质。
#
# selectedValue = 5
# modificationCost = 1
# 得分为 5 - 1 = 4
# 示例 2：
#
# 输入： nums = [1,2,3], maxVal = 4
#
# 输出： 3
#
# 解释：
#
# 不需要进行任何修改。选择 nums[2] = 3，因为它与 1 和 2 互质。
#
# selectedValue = 3
# modificationCost = 0
# 得分为 3 - 0 = 3
# 示例 3：
#
# 输入： nums = [2,2], maxVal = 1
#
# 输出： 1
#
# 解释：
#
# 将 nums[0] 从 2 更改为 1，代价为 1。选择 nums[1] = 2，因为它与 1 互质。
#
# selectedValue = 2
# modificationCost = 1
# 得分为 2 - 1 = 1
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# 1 <= maxVal <= 105

from leetcode.allcode.competition.mypackage import *


# 总体思路，枚举每个可能的 selectedValue, 范围<=max(max(nums), maxVal)
# 计算 nums 中与 selectedValue 不互质的元素个数C，计算它们的差，用差去更新ans
# C的计算，需要枚举 selectedValue 所有因子p[i]，根据容斥原理，C=p[i]*mu[p[i]]
# 其中mu[p[i]]是容斥原理的一个系数，可能是1或-1，取决于p[i]中包含质因子的个数
# 这个mu[p[i]] 可以用莫比乌斯函数计算得到

# 一个数的所有因子，可以预处理得到
# mu可以预处理得到
# 某个x是否存在于nums中，一共有几个，可以提前构造好
# 多个nums[i]拥有因子p，可以提前计算出来


MX = 100_001

# 计算所有莫比乌斯函数值，即容斥原理的系数
# 对于没有平方质因子的数x，其mu(x)=(-1)^质因子个数
# 有平方质因子的数x，其mu(x)=0
# 预处理莫比乌斯函数
# 当 n > 1 时，sum_{d|n} mu[d] = 0
# 所以 mu[n] = -sum_{d|n ∧ d<n} mu[d]
mu = [0] * MX
mu[1] = 1
for i in range(1, MX):
    for j in range(i * 2, MX, i):
        mu[j] -= mu[i]  # i 是 j 的真因子

# MX = 10
divisors = [[] for _ in range(MX)]  # divisors[i] 表示 i 的所有因子
for i in range(2, MX):  # 预处理每个数的所有因子，时间复杂度 O(MlogM)，M=1e5
    for j in range(i, MX, i):
        divisors[j].append(i)

class Solution:
    def maxScore(self, nums: List[int], maxVal: int) -> int:
        n = len(nums)
        counter = Counter(nums)
        mx_n = max(nums)
        mx = max(mx_n, maxVal)
        fc = [0] * (mx + 1)  # 包含因子i的元素个数 fc[i]
        for i in range(2, mx + 1):
            for j in range(i, mx + 1, i):
                fc[i] += counter[j]

        c1 = nums.count(1)
        # 先假设 selectedValue 为1，所有数都已经与1互质
        if c1 > 0:
            ans = 1
        else:
            ans = 1 - 1

        for sel in range(2, mx + 1):
            cnt = 0  # nums中于sel不互质的元素个数
            if counter[sel] == 0 and sel > maxVal: continue
            for f in divisors[sel]:
                cnt += -mu[f] * fc[f]
            if counter[sel]:
                # sel 在nums中存在，这个数本身不需要变换，但又被统计到cnt中了，因此要减掉
                cnt -= 1
            elif cnt == 0:
                # sel 在nums中存在，并且没有元素与其不互质，还是需要再找一个元素出来变成sel，因此要加一
                cnt += 1
            ans = max(ans, sel - cnt)
        return ans


so = Solution()
print(so.maxScore(nums = [42], maxVal = 312))
print(so.maxScore(nums = [1000], maxVal = 1000))
print(so.maxScore(nums = [3,4,6], maxVal = 5))




