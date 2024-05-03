# 给定一个有 n 个整数的数组 nums ，如果能找到满足以下条件的三元组  (i, j, k)  则返回 true ：
#
# 0 < i, i + 1 < j, j + 1 < k < n - 1
# 子数组 (0, i - 1) ， (i + 1, j - 1) ， (j + 1, k - 1) ， (k + 1, n - 1) 的和应该相等。
# 这里我们定义子数组 (l, r) 表示原数组从索引为 l 的元素开始至索引为 r 的元素。
#
#
#
# 示例 1:
#
# 输入: nums = [1,2,1,2,1,2,1]
# 输出: True
# 解释:
# i = 1, j = 3, k = 5.
# sum(0, i - 1) = sum(0, 0) = 1
# sum(i + 1, j - 1) = sum(2, 2) = 1
# sum(j + 1, k - 1) = sum(4, 4) = 1
# sum(k + 1, n - 1) = sum(6, 6) = 1
# 示例 2:
#
# 输入: nums = [1,2,1,2,1,2,1,2]
# 输出: false
#
#
# 提示:
#
# n == nums.length
# 1 <= n <= 2000
# -106 <= nums[i] <= 106

from leetcode.allcode.competition.mypackage import *

class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 7: return False
        s = list(accumulate(nums, initial=0))
        index = defaultdict(list)   # 记录值为x的下标列表 counter[x]
        for i, x in enumerate(nums):
            index[x].append(i)
        for j in range(3, n - 3):  # 枚举下标 j
            for i in range(1, j - 1):  # 枚举下标 i
                if s[i] != s[j] - s[i + 1]: continue
                s2 = s[j] - nums[i]  # 两个小区间之和
                right = s[n] - s[j + 1]
                del_right = right - s2  # 从j+1开始的右侧元素需要删掉一个值为 del_right 的元素，即nums[k]的值
                idx = bisect_left(index[del_right], j + 2)
                ss = s[i]  # 每个小区间的和
                while idx < len(index[del_right]):
                    k = index[del_right][idx]
                    if j + 1 < k < n - 1 and s[k] - s[j + 1] == ss == s[n] - s[k + 1]:
                        return True
                    idx += 1
        return False

so = Solution()
print(so.splitArray(nums = [1,2,1,2,1,2,1]))
print(so.splitArray(nums = [1,2,1,2,1,2,1,2]))




