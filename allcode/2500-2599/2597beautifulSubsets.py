# 给你一个由正整数组成的数组 nums 和一个 正 整数 k 。
#
# 如果 nums 的子集中，任意两个整数的绝对差均不等于 k ，则认为该子数组是一个 美丽 子集。
#
# 返回数组 nums 中 非空 且 美丽 的子集数目。
#
# nums 的子集定义为：可以经由 nums 删除某些元素（也可能不删除）得到的一个数组。只有在删除元素时选择的索引不同的情况下，两个子集才会被视作是不同的子集。
#
#
#
# 示例 1：
#
# 输入：nums = [2,4,6], k = 2
# 输出：4
# 解释：数组 nums 中的美丽子集有：[2], [4], [6], [2, 6] 。
# 可以证明数组 [2,4,6] 中只存在 4 个美丽子集。
# 示例 2：
#
# 输入：nums = [1], k = 1
# 输出：1
# 解释：数组 nums 中的美丽数组有：[1] 。
# 可以证明数组 [1] 中只存在 1 个美丽子集。
#
#
# 提示：
#
# 1 <= nums.length <= 20
# 1 <= nums[i], k <= 1000

from leetcode.allcode.competition.mypackage import *


class Solution:
    def beautifulSubsets1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        ss = set()
        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) == k:
                    ss.add((i, j))
        def judge(mask):
            for x, y in ss:
                if mask & (1 << x) and mask & (1 << y):
                    return False
            return True

        for i in range(1, 2 ** n):
            if judge(i):
                ans += 1
        return ans


    def beautifulSubsets2(self, nums: List[int], k: int) -> int:
        # 2023/4/1  子集型回溯，性能和上面的暴力差不多
        n = len(nums)
        ct = [0] * (max(nums) + k + 1)
        ans = -1  # 去掉空集

        def dfs(idx):
            nonlocal ans
            if idx == n:
                ans += 1
                return
            dfs(idx + 1)  # 不选 nums[i]

            if (nums[idx] - k >= 0 and ct[nums[idx] - k] > 0) or ct[nums[idx] + k] > 0:
                return

            # 选 nums[i]
            ct[nums[idx]] += 1
            dfs(idx + 1)
            ct[nums[idx]] -= 1  # 恢复现场
        dfs(0)
        return ans

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # 2023/4/1  取模分组 + DP，性能高于前两个很多
        d = defaultdict(Counter)  # d[i] 表示模k余i的一个分组，每个分组统计d[i][j]的出现次数
        for x in nums:
            m = x % k
            d[m][x] += 1
        ans = 1
        for counter in d.values():
            l = sorted([[x, cnt] for x, cnt in counter.items()])

            def func(ll):  # 统计每个分组内有多少种美丽子集
                def t(x): # 2 ^ x
                    return 2 << (x - 1)
                n = len(ll)
                f = t(ll[0][1]) - 1  # 前 i 个数中，包含 ll[i][0] 的总数
                g = 1  # 前 i 个数中，不包含包含 ll[i][0] 的总数
                for i in range(1, n):
                    if ll[i][0] - ll[i - 1][0] == k:
                        f, g = g * (t(ll[i][1]) - 1), f + g
                    else:
                        f, g = (f + g) * (t(ll[i][1]) - 1), f + g
                return f + g
            ans *= func(l)

        return ans - 1




so = Solution()
print(so.beautifulSubsets([4,2],1))  # 3
print(so.beautifulSubsets([9,5], 9))  # 3
print(so.beautifulSubsets([9,5,7,10,6,2], 9))  # 63
print(so.beautifulSubsets(nums = [2,4,6], k = 2))  # 4
print(so.beautifulSubsets([1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000], 1))
print(so.beautifulSubsets(nums = [1], k = 1))  # 1




