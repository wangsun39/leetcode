# 你需要在一个集合里动态记录 ID 的出现频率。给你两个长度都为 n 的整数数组 nums 和 freq ，nums 中每一个元素表示一个 ID ，对应的 freq 中的元素表示这个 ID 在集合中此次操作后需要增加或者减少的数目。
#
# 增加 ID 的数目：如果 freq[i] 是正数，那么 freq[i] 个 ID 为 nums[i] 的元素在第 i 步操作后会添加到集合中。
# 减少 ID 的数目：如果 freq[i] 是负数，那么 -freq[i] 个 ID 为 nums[i] 的元素在第 i 步操作后会从集合中删除。
# 请你返回一个长度为 n 的数组 ans ，其中 ans[i] 表示第 i 步操作后出现频率最高的 ID 数目 ，如果在某次操作后集合为空，那么 ans[i] 为 0 。
#
#
#
# 示例 1：
#
# 输入：nums = [2,3,2,1], freq = [3,2,-3,1]
#
# 输出：[3,3,2,2]
#
# 解释：
#
# 第 0 步操作后，有 3 个 ID 为 2 的元素，所以 ans[0] = 3 。
# 第 1 步操作后，有 3 个 ID 为 2 的元素和 2 个 ID 为 3 的元素，所以 ans[1] = 3 。
# 第 2 步操作后，有 2 个 ID 为 3 的元素，所以 ans[2] = 2 。
# 第 3 步操作后，有 2 个 ID 为 3 的元素和 1 个 ID 为 1 的元素，所以 ans[3] = 2 。
#
# 示例 2：
#
# 输入：nums = [5,5,3], freq = [2,-2,1]
#
# 输出：[2,0,1]
#
# 解释：
#
# 第 0 步操作后，有 2 个 ID 为 5 的元素，所以 ans[0] = 2 。
# 第 1 步操作后，集合中没有任何元素，所以 ans[1] = 0 。
# 第 2 步操作后，有 1 个 ID 为 3 的元素，所以 ans[2] = 1 。
#
#
#
# 提示：
#
# 1 <= nums.length == freq.length <= 105
# 1 <= nums[i] <= 105
# -105 <= freq[i] <= 105
# freq[i] != 0
# 输入保证任何操作后，集合中的元素出现次数不会为负数。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        counter = Counter()
        sl = SortedList()
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            x, f = nums[i], freq[i]
            if x in counter:
                sl.remove(counter[x])
            counter[x] += f
            sl.add(counter[x])
            ans[i] = sl[-1]
        return ans



so = Solution()
print(so.mostFrequentIDs(nums = [2,3,2,1], freq = [3,2,-3,1]))
print(so.mostFrequentIDs(nums = [5,5,3], freq = [2,-2,1]))




