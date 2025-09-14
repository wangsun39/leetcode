# 我们称一个数字字符串是 好数字 当它满足（下标从 0 开始）偶数 下标处的数字为 偶数 且 奇数 下标处的数字为 质数 （2，3，5 或 7）。
#
# 比方说，"2582" 是好数字，因为偶数下标处的数字（2 和 8）是偶数且奇数下标处的数字（5 和 2）为质数。但 "3245" 不是 好数字，因为 3 在偶数下标处但不是偶数。
# 给你一个整数 n ，请你返回长度为 n 且为好数字的数字字符串 总数 。由于答案可能会很大，请你将它对 109 + 7 取余后返回 。
#
# 一个 数字字符串 是每一位都由 0 到 9 组成的字符串，且可能包含前导 0 。
#
#
#
# 示例 1：
#
# 输入：n = 1
# 输出：5
# 解释：长度为 1 的好数字包括 "0"，"2"，"4"，"6"，"8" 。
# 示例 2：
#
# 输入：n = 4
# 输出：400
# 示例 3：
#
# 输入：n = 50
# 输出：564908303
#
#
# 提示：
#
# 1 <= n <= 1015


from leetcode.allcode.competition.mypackage import *

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        m = len(paths)
        hi = min(len(p) for p in paths)

        MOD1 = 1000000000039  # 找了个很大的质数，否则过不去
        MOD2 = 10 ** 9 + 7
        BASE1 = random.randint(8 * 10 ** 8, 9 * 10 ** 8)  # 随机 BASE，防止 hack
        pow_base1 = [1] + [0] * hi  # pow_base[i] = BASE^i
        BASE2 = random.randint(8 * 10 ** 8, 9 * 10 ** 8)  # 随机 BASE，防止 hack
        pow_base2 = [1] + [0] * hi  # pow_base[i] = BASE^i
        for i in range(hi):
            pow_base1[i + 1] = pow_base1[i] * BASE1 % MOD1
            pow_base2[i + 1] = pow_base2[i] * BASE2 % MOD2

        def check(val):
            hash_paths1 = [set() for _ in range(m)]  # 计算每条路径的长为val的所有子串的hash值
            hash_paths2 = [set() for _ in range(m)]  # 计算每条路径的长为val的所有子串的hash值

            for i in range(m):
                cur1 = cur2 = 0
                n1 = len(paths[i])  # 长度为val的子串有 n1-val+1 个
                for j in range(val):
                    cur1 += paths[i][val - 1 - j] * pow_base1[j]
                    cur2 += paths[i][val - 1 - j] * pow_base2[j]
                hash_paths1[i].add(cur1 % MOD1)
                hash_paths2[i].add(cur2 % MOD2)
                for j in range(1, n1 - val + 1):
                    cur1 = cur1 * BASE1 + paths[i][j + val - 1] - pow_base1[val] * paths[i][j - 1]
                    cur1 %= MOD1
                    hash_paths1[i].add(cur1)
                    cur2 = cur2 * BASE2 + paths[i][j + val - 1] - pow_base2[val] * paths[i][j - 1]
                    cur2 %= MOD2
                    hash_paths2[i].add(cur2)
                if i == 0:
                    insect1 = hash_paths1[i]
                    insect2 = hash_paths2[i]
                else:
                    insect1 &= hash_paths1[i]
                    insect2 &= hash_paths2[i]
                    if len(insect1) == 0 or len(insect2) == 0:
                        return False
            return True

        lo, hi = 0, hi + 1
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid
        return lo

so = Solution()
print(so.longestCommonSubpath(n = 5, paths = [[0,1,2,3,4],[4,3,2,1,0]]))
print(so.longestCommonSubpath(n = 5, paths = [[1,2,3,4],[4,1,2,3],[4]]))
print(so.longestCommonSubpath(n = 5, paths = [[0,1,2,3,4],
                     [2,3,4],
                     [4,0,1,2,3]]))





