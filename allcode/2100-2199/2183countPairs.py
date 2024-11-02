# 给你一个下标从 0 开始、长度为 n 的整数数组 nums 和一个整数 k ，返回满足下述条件的下标对 (i, j) 的数目：
#
# 0 <= i < j <= n - 1 且
# nums[i] * nums[j] 能被 k 整除。
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,4,5], k = 2
# 输出：7
# 解释：
# 共有 7 对下标的对应积可以被 2 整除：
# (0, 1)、(0, 3)、(1, 2)、(1, 3)、(1, 4)、(2, 3) 和 (3, 4)
# 它们的积分别是 2、4、6、8、10、12 和 20 。
# 其他下标对，例如 (0, 2) 和 (2, 4) 的乘积分别是 3 和 15 ，都无法被 2 整除。
# 示例 2：
#
# 输入：nums = [1,2,3,4], k = 5
# 输出：0
# 解释：不存在对应积可以被 5 整除的下标对。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i], k <= 105
import math

from leetcode.allcode.competition.mypackage import *

MX = 10 ** 5 + 1
divisors = [[] for _ in range(MX)]  # divisors[i] 表示 i 的所有因子
for i in range(1, MX):  # 预处理每个数的所有因子，时间复杂度 O(MlogM)，M=1e5
    for j in range(i, MX, i):
        divisors[j].append(i)


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt = defaultdict(int)  # cnt[i] 表示处理的过的数中含有因子i的数的个数
        for x in nums:
            y = k // math.gcd(x, k)  # x 缺少 的因子
            ans += cnt[y]
            for v in divisors[x]:
                cnt[v] += 1
        return ans



so = Solution()
print(so.countPairs(nums = [8,10,2,5,9,6,3,8,2], k = 6))   # 18
print(so.countPairs(nums = [1,2,3,4,5], k = 2))
print(so.countPairs(nums = [1,2,3,4], k = 5))




