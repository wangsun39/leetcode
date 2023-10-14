# 给你一个下标从 0 开始长度为 n 的数组 nums 。
#
# 每一秒，你可以对数组执行以下操作：
#
# 对于范围在 [0, n - 1] 内的每一个下标 i ，将 nums[i] 替换成 nums[i] ，nums[(i - 1 + n) % n] 或者 nums[(i + 1) % n] 三者之一。
# 注意，所有元素会被同时替换。
#
# 请你返回将数组 nums 中所有元素变成相等元素所需要的 最少 秒数。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,1,2]
# 输出：1
# 解释：我们可以在 1 秒内将数组变成相等元素：
# - 第 1 秒，将每个位置的元素分别变为 [nums[3],nums[1],nums[3],nums[3]] 。变化后，nums = [2,2,2,2] 。
# 1 秒是将数组变成相等元素所需要的最少秒数。
# 示例 2：
#
# 输入：nums = [2,1,3,3,2]
# 输出：2
# 解释：我们可以在 2 秒内将数组变成相等元素：
# - 第 1 秒，将每个位置的元素分别变为 [nums[0],nums[2],nums[2],nums[2],nums[3]] 。变化后，nums = [2,3,3,3,3] 。
# - 第 2 秒，将每个位置的元素分别变为 [nums[1],nums[1],nums[2],nums[3],nums[4]] 。变化后，nums = [3,3,3,3,3] 。
# 2 秒是将数组变成相等元素所需要的最少秒数。
# 示例 3：
#
# 输入：nums = [5,5,5,5]
# 输出：0
# 解释：不需要执行任何操作，因为一开始数组中的元素已经全部相等。
#
#
# 提示：
#
# 1 <= n == nums.length <= 105
# 1 <= nums[i] <= 109

from leetcode.allcode.competition.mypackage import *


class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        n = len(items)
        items.sort()
        items1, items2 = items[n - k:], items[:n - k][::-1]  # items1 顺序， items2 逆序
        n2 = len(items2)
        counter = Counter(it[1] for it in items1)
        j = 0  # 对应 items2 的下标
        cur = ans = sum(it[0] for it in items1) + len(counter) ** 2
        # 尝试类别的所有可能 (>=len(counter))， 计算其中的最大值
        for i in range(k):
            p1, c1 = items1[i]
            if counter[c1] == 1:
                continue
            while j < len(items2) and counter[items2[j][1]] > 0:
                j += 1
            if j >= n2:
                break
            # 尝试调换 items1[i] 和 items2[j]
            cnt = len(counter)
            p2, c2 = items2[j]
            items1[i] = items2[j]
            counter[c1] -= 1
            counter[c2] = 1
            cur += (p2 + cnt * 2 + 1 - p1)  # 计算差值
            ans = max(ans, cur)

        return ans



so = Solution()
print(so.findMaximumElegance(items = [[3,2],[5,1],[10,1]], k = 2))
print(so.findMaximumElegance(items = [[10,1],[10,1],[10,1],[10,1],[10,1],[10,1],[10,1],[10,1],[10,1],[10,1],[3,2],[3,3],[3,4],[3,5],[3,6],[3,7],[3,8],[3,9],[3,10],[3,11]], k = 10))
print(so.findMaximumElegance(items = [[3,4],[8,4],[2,2],[1,3]], k = 2))
print(so.findMaximumElegance(items = [[5,1],[6,1],[8,1]], k = 2))
print(so.findMaximumElegance(items = [[3,1],[3,1],[2,2],[5,3]], k = 3))
print(so.findMaximumElegance(items = [[1,1],[2,1],[3,1]], k = 3))




