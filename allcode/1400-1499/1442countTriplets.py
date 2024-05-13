# 给你一个整数数组 arr 。
#
# 现需要从数组中取三个下标 i、j 和 k ，其中 (0 <= i < j <= k < arr.length) 。
#
# a 和 b 定义如下：
#
# a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
# b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
# 注意：^ 表示 按位异或 操作。
#
# 请返回能够令 a == b 成立的三元组 (i, j , k) 的数目。
#
#
#
# 示例 1：
#
# 输入：arr = [2,3,1,6,7]
# 输出：4
# 解释：满足题意的三元组分别是 (0,1,2), (0,2,2), (2,3,4) 以及 (2,4,4)
# 示例 2：
#
# 输入：arr = [1,1,1,1,1]
# 输出：10
# 示例 3：
#
# 输入：arr = [2,3]
# 输出：0
# 示例 4：
#
# 输入：arr = [1,3,5,7,9]
# 输出：3
# 示例 5：
#
# 输入：arr = [7,11,12,9,5,2,7,17,22]
# 输出：8
#
#
# 提示：
#
# 1 <= arr.length <= 300
# 1 <= arr[i] <= 10^8

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        right = [Counter() for _ in range(n)]  # right[i][x] 表示以 arr[i]为左端点的子串，异或值为x的子串个数
        for i, x in enumerate(arr):
            cur = 0
            for j in range(i, n):
                cur ^= arr[j]
                right[i][cur] += 1
        ans = 0
        for i in range(n):
            cur = 0
            for j in range(i + 1, n):
                cur ^= arr[j - 1]
                ans += right[j][cur]
        return ans

    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        s = [0]  # 前缀异或和
        # 性质： 区间[i,j)的异或和= s[j] ^ s[i]
        # 那么 [i,j) 和 [j,k+1) 异或和相等，也就是 s[j] ^ s[k+1] == s[j] ^ s[i]，即 s[k+1] == s[i]，这就与j无关了
        # 枚举 k + 1， 找i用哈希
        for i in range(n):
            s.append(arr[i] ^ s[-1])



so = Solution()
print(so.countTriplets([2,3,1,6,7]))
print(so.countTriplets([1,1,1,1,1]))
print(so.countTriplets([2,3]))
print(so.countTriplets([1,3,5,7,9]))
print(so.countTriplets([7,11,12,9,5,2,7,17,22]))


