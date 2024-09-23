# 给你一个字符串数组 words 和一个字符串 target。
#
# 如果字符串 x 是 words 中 任意 字符串的
# 前缀
# ，则认为 x 是一个 有效 字符串。
#
# 现计划通过 连接 有效字符串形成 target ，请你计算并返回需要连接的 最少 字符串数量。如果无法通过这种方式形成 target，则返回 -1。
#
#
#
# 示例 1：
#
# 输入： words = ["abc","aaaaa","bcdef"], target = "aabcdabc"
#
# 输出： 3
#
# 解释：
#
# target 字符串可以通过连接以下有效字符串形成：
#
# words[1] 的长度为 2 的前缀，即 "aa"。
# words[2] 的长度为 3 的前缀，即 "bcd"。
# words[0] 的长度为 3 的前缀，即 "abc"。
# 示例 2：
#
# 输入： words = ["abababab","ab"], target = "ababaababa"
#
# 输出： 2
#
# 解释：
#
# target 字符串可以通过连接以下有效字符串形成：
#
# words[0] 的长度为 5 的前缀，即 "ababa"。
# words[0] 的长度为 5 的前缀，即 "ababa"。
# 示例 3：
#
# 输入： words = ["abcdef"], target = "xyz"
#
# 输出： -1
#
#
#
# 提示：
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 5 * 104
# 输入确保 sum(words[i].length) <= 105.
# words[i]  只包含小写英文字母。
# 1 <= target.length <= 5 * 104
# target  只包含小写英文字母。

from leetcode.allcode.competition.mypackage import *


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)

        # 哈希函数 hash(s) = s[0] * base^(n-1) + s[1] * base^(n-2) + ... + s[n-2] * base + s[n-1]
        base = random.randint(8 * 10 ** 8, 9 * 10 ** 8)
        MOD = 10 ** 9 + 7
        pow_base = [1] + [0] * n  # base ** i
        pre_hash = [0] * (n + 1)  # hash(target[:i])
        for i, b in enumerate(target):
            pow_base[i + 1] = pow_base[i] * base % MOD
            pre_hash[i + 1] = (pre_hash[i] * base + ord(b)) % MOD

        # 计算子串 target[l:r] 的哈希值，注意这是左闭右开区间 [l,r)
        # 计算方法类似前缀和
        def sub_hash(l: int, r: int) -> int:
            return (pre_hash[r] + MOD - pre_hash[l] * pow_base[r - l]) % MOD

        # 保存每个 words[i] 的每个前缀的哈希值，按照长度分组
        max_len = max(map(len, words))
        sets = [set() for _ in range(max_len)]
        for w in words:
            h = 0
            for i, b in enumerate(w):
                h = (h * base + ord(b)) % MOD
                sets[i].add(h)

        mx_matches = [0] * n  # 从target[i]开始在words中匹配到的最长前缀长度
        for l in range(n):
            mx_len = min(n - l, max_len)
            check = lambda v: sub_hash(l, l + v + 1) not in sets[v]
            mx_matches[l] = bisect_left(range(mx_len), True, key=check)

        # 跳跃游戏
        ans = nxt_r = cur_r = 0
        for i in range(n):
            nxt_r = max(nxt_r, i + mx_matches[i])
            if i == cur_r:
                if i == nxt_r:
                    return -1
                cur_r = nxt_r
                ans += 1
        return ans




so = Solution()
print(so.minValidStrings(words=["abc", "aaaaa", "bcdef"], target="aabcdabc"))
print(so.minValidStrings(words=["abababab", "ab"], target="ababaababa"))
print(so.minValidStrings(words=["abcdef"], target="xyz"))
