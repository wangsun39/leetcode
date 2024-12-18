
from leetcode.allcode.competition.mypackage import *


class Solution:

    def beautifulSplits(self, nums: List[int]) -> int:
        n = len(nums)

        # 整型数组的哈希
        def hash1(start, base, MOD):
            # 哈希函数 hash(s) = s[0] * base^(n-1) + s[1] * base^(n-2) + ... + s[n-2] * base + s[n-1]
            h = []
            pow_base = [1] + [0] * n  # base ** i
            vp = 0  # 计算pattern的hash值
            for i, b in enumerate(nums[start:], start):
                pow_base[i + 1] = pow_base[i] * base % MOD
                vp = (vp * base + b) % MOD
                h.append(vp)
            return h

        base1 = random.randint(8 * 10 ** 8, 9 * 10 ** 8)
        MOD1 = 10 ** 9 + 7

        nums_hash = []
        for i in range(n):
            nums_hash.append(hash(i, base1, MOD1))

    # 字符串哈希
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)

        # 多项式字符串哈希（方便计算子串哈希值）
        # 哈希函数 hash(s) = s[0] * BASE^(n-1) + s[1] * BASE^(n-2) + ... + s[n-2] * BASE + s[n-1]
        MOD = 1_070_777_777
        BASE = random.randint(8 * 10 ** 8, 9 * 10 ** 8)  # 随机 BASE，防止 hack
        pow_base = [1] + [0] * n  # pow_base[i] = BASE^i
        pre_hash = [0] * (n + 1)  # 前缀哈希值 pre_hash[i] = hash(s[:i])
        for i, b in enumerate(target):
            pow_base[i + 1] = pow_base[i] * BASE % MOD
            pre_hash[i + 1] = (pre_hash[i] * BASE + ord(b)) % MOD  # 秦九韶算法计算多项式哈希

        # 计算子串 target[l:r] 的哈希值，注意这是左闭右开区间 [l,r)
        # 计算方法类似前缀和
        def sub_hash(l: int, r: int) -> int:
            return (pre_hash[r] - pre_hash[l] * pow_base[r - l]) % MOD


