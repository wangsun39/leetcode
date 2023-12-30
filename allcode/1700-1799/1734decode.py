# 给你一个整数数组 perm ，它是前 n 个正整数的排列，且 n 是个 奇数 。
#
# 它被加密成另一个长度为 n - 1 的整数数组 encoded ，满足 encoded[i] = perm[i] XOR perm[i + 1] 。比方说，如果 perm = [1,3,2] ，那么 encoded = [2,1] 。
#
# 给你 encoded 数组，请你返回原始数组 perm 。题目保证答案存在且唯一。
#
#
#
# 示例 1：
#
# 输入：encoded = [3,1]
# 输出：[1,2,3]
# 解释：如果 perm = [1,2,3] ，那么 encoded = [1 XOR 2,2 XOR 3] = [3,1]
# 示例 2：
#
# 输入：encoded = [6,5,4,6]
# 输出：[2,4,1,5,3]
#
#
# 提示：
#
# 3 <= n < 105
# n 是奇数。
# encoded.length == n - 1

from leetcode.allcode.competition.mypackage import *

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded)
        sup = [0] * n  # 设元素数组为a，sup依次记录a[0]^a[1],a[0]^a[2],...,a[0]^a[n]
        sup[0] = encoded[0]
        for i in range(1, n):
            sup[i] = sup[i - 1] ^ encoded[i]
        s = set(sup)
        nums = [0] * (n + 1)
        for i in range(1, 10 ** 5):  # a[0]不能与任何sup的元素相同，否则某个a[i]将会是0
            if i not in s:
                nums[0] = i
                break
        for i in range(n):
            nums[i + 1] = nums[0] ^ sup[i]
        return nums



so = Solution()
print(so.decode(encoded = [3,1]))
print(so.decode(encoded = [6,5,4,6]))




