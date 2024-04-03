# 给你一个下标从 0 开始长度为 n 的整数数组 nums ，和一个下标从 0 开始长度为 m 的整数数组 pattern ，pattern 数组只包含整数 -1 ，0 和 1 。
#
# 大小为 m + 1 的子数组 nums[i..j] 如果对于每个元素 pattern[k] 都满足以下条件，那么我们说这个子数组匹配模式数组 pattern ：
#
# 如果 pattern[k] == 1 ，那么 nums[i + k + 1] > nums[i + k]
# 如果 pattern[k] == 0 ，那么 nums[i + k + 1] == nums[i + k]
# 如果 pattern[k] == -1 ，那么 nums[i + k + 1] < nums[i + k]
# 请你返回匹配 pattern 的 nums 子数组的 数目 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,4,5,6], pattern = [1,1]
# 输出：4
# 解释：模式 [1,1] 说明我们要找的子数组是长度为 3 且严格上升的。在数组 nums 中，子数组 [1,2,3] ，[2,3,4] ，[3,4,5] 和 [4,5,6] 都匹配这个模式。
# 所以 nums 中总共有 4 个子数组匹配这个模式。
# 示例 2：
#
# 输入：nums = [1,4,4,1,3,5,5,3], pattern = [1,0,-1]
# 输出：2
# 解释：这里，模式数组 [1,0,-1] 说明我们需要找的子数组中，第一个元素小于第二个元素，第二个元素等于第三个元素，第三个元素大于第四个元素。在 nums 中，子数组 [1,4,4,1] 和 [3,5,5,3] 都匹配这个模式。
# 所以 nums 中总共有 2 个子数组匹配这个模式。
#
#
# 提示：
#
# 2 <= n == nums.length <= 106
# 1 <= nums[i] <= 109
# 1 <= m == pattern.length < n
# -1 <= pattern[i] <= 1

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        diff = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] - nums[i] > 0:
                diff[i] = 1
            elif nums[i + 1] - nums[i] < 0:
                diff[i] = -1
            else:
                diff[i] = 0
        def build_prefix_table(pattern):
            length = len(pattern)
            lps = [0] * length  # 初始化前缀表

            i = 1
            length_of_longest_prefix = 0
            while i < length:
                if pattern[i] == pattern[length_of_longest_prefix]:
                    length_of_longest_prefix += 1
                    lps[i] = length_of_longest_prefix
                    i += 1
                else:
                    if length_of_longest_prefix != 0:
                        length_of_longest_prefix = lps[length_of_longest_prefix - 1]
                    else:
                        lps[i] = 0
                        i += 1

            return lps

        def kmp_search(text, pattern):
            n = len(text)
            m = len(pattern)
            indices = []  # 用于存储匹配成功的起始下标


            lps = build_prefix_table(pattern)

            i, j = 0, 0
            while i < n:
                if text[i] == pattern[j]:
                    i += 1
                    j += 1

                    if j == m:
                        indices.append(i - j)
                        j = lps[j - 1]
                else:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1

            return indices
        l = kmp_search(diff, pattern)
        return len(l)




so = Solution()
print(so.countMatchingSubarrays(nums = [1,2,3,4,5,6], pattern = [1,1]))
print(so.countMatchingSubarrays(nums = [1,4,4,1,3,5,5,3], pattern = [1,0,-1]))
print(so.countMatchingSubarrays(nums = [1,2,3,4,5,6], pattern = [1,1]))





