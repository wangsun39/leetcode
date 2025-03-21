# 给你一个整数数组 arr，请你将该数组分隔为长度 最多 为 k 的一些（连续）子数组。分隔完成后，每个子数组的中的所有值都会变为该子数组中的最大值。
#
# 返回将数组分隔变换后能够得到的元素最大和。本题所用到的测试用例会确保答案是一个 32 位整数。
#
#
#
# 示例 1：
#
# 输入：arr = [1,15,7,9,2,5,10], k = 3
# 输出：84
# 解释：数组变为 [15,15,15,9,10,10,10]
# 示例 2：
#
# 输入：arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
# 输出：83
# 示例 3：
#
# 输入：arr = [1], k = 1
# 输出：1
#
#
# 提示：
#
# 1 <= arr.length <= 500
# 0 <= arr[i] <= 109
# 1 <= k <= arr.length

from leetcode.allcode.competition.mypackage import *

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        MOD = 1_070_777_777
        BASE1 = random.randint(8 * 10 ** 8, 9 * 10 ** 8)  # 随机 BASE，防止 hack
        BASE2 = random.randint(8 * 10 ** 8, 9 * 10 ** 8)  # 随机 BASE，防止 hack
        pow_base1 = [1] + [0] * n  # pow_base1[i] = BASE^i
        pre_hash1 = [0] * (n + 1)  # 前缀哈希值 pre_hash1[i] = hash(s[:i])
        for i, b in enumerate(s):
            pow_base1[i + 1] = pow_base1[i] * BASE1 % MOD
            pre_hash1[i + 1] = (pre_hash1[i] * BASE1 + ord(b)) % MOD  # 秦九韶算法计算多项式哈希
        pow_base2 = [1] + [0] * n  # pow_base[i] = BASE^i
        pre_hash2 = [0] * (n + 1)  # 前缀哈希值 pre_hash[i] = hash(s[:i])
        for i, b in enumerate(s):
            pow_base2[i + 1] = pow_base2[i] * BASE2 % MOD
            pre_hash2[i + 1] = (pre_hash2[i] * BASE2 + ord(b)) % MOD  # 秦九韶算法计算多项式哈希

        def sub_hash1(l: int, r: int) -> int:
            return (pre_hash1[r] - pre_hash1[l] * pow_base1[r - l]) % MOD
        def sub_hash2(l: int, r: int) -> int:
            return (pre_hash2[r] - pre_hash2[l] * pow_base2[r - l]) % MOD

        def check(m):  # 检查是否存在长度为val的子串满足条件
            se1 = set()  # 所有长度为val的子串的hash值
            se2 = set()  # 所有长度为val的子串的hash值
            for i in range(n - m + 1):
                v1 = sub_hash1(i, i + m)
                v2 = sub_hash2(i, i + m)
                if v1 in se1 and v2 in se2:
                    return s[i: i + m]
                se1.add(v1)
                se2.add(v2)
            return None


        ans = check(n - 1)
        if ans:
            return ans

        ans = check(1)
        if not ans: return ''
        lo, hi = 1, n - 1
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            v = check(mid)
            if v:
                lo = mid
                ans = v
            else:
                hi = mid
        return ans



obj = Solution()
print(obj.longestDupSubstring(s = "banana"))

