# 我们有一个非负整数数组 arr 。
#
# 对于每个（连续的）子数组 sub = [arr[i], arr[i + 1], ..., arr[j]] （ i <= j），我们对 sub 中的每个元素进行按位或操作，获得结果 arr[i] | arr[i + 1] | ... | arr[j] 。
#
# 返回可能结果的数量。 多次出现的结果在最终答案中仅计算一次。
#
#
#
# 示例 1：
#
# 输入：arr = [0]
# 输出：1
# 解释：
# 只有一个可能的结果 0 。
# 示例 2：
#
# 输入：arr = [1,1,2]
# 输出：3
# 解释：
# 可能的子数组为 [1]，[1]，[2]，[1, 1]，[1, 2]，[1, 1, 2]。
# 产生的结果为 1，1，2，1，3，3 。
# 有三个唯一值，所以答案是 3 。
# 示例 3：
#
# 输入：arr = [1,2,4]
# 输出：6
# 解释：
# 可能的结果是 1，2，3，4，6，以及 7 。
#
#
# 提示：
# 1 <= nums.length <= 5 * 104
# 0 <= nums[i] <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        s1 = set()  # 记录以每个arr[i]结尾的子数组能获取到的所有按位或值
        for x in arr:
            s2 = {x}
            for y in s1:
                s2.add(y | x)  # s2中的个数不会超过2^32
            ans |= s2
            s1 = s2
        return len(ans)




so = Solution()
print(so.subarrayBitwiseORs(arr = [0]))
print(so.subarrayBitwiseORs(arr = [1,1,2]))
print(so.subarrayBitwiseORs(arr = [1,2,4]))




