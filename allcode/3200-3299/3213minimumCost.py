# 给你一个字符串 target、一个字符串数组 words 以及一个整数数组 costs，这两个数组长度相同。
#
# 设想一个空字符串 s。
#
# 你可以执行以下操作任意次数（包括 零 次）：
#
# 选择一个在范围  [0, words.length - 1] 的索引 i。
# 将 words[i] 追加到 s。
# 该操作的成本是 costs[i]。
# 返回使 s 等于 target 的 最小 成本。如果不可能，返回 -1。
#
#
#
# 示例 1：
#
# 输入： target = "abcdef", words = ["abdef","abc","d","def","ef"], costs = [100,1,1,10,5]
#
# 输出： 7
#
# 解释：
#
# 选择索引 1 并以成本 1 将 "abc" 追加到 s，得到 s = "abc"。
# 选择索引 2 并以成本 1 将 "d" 追加到 s，得到 s = "abcd"。
# 选择索引 4 并以成本 5 将 "ef" 追加到 s，得到 s = "abcdef"。
# 示例 2：
#
# 输入： target = "aaaa", words = ["z","zz","zzz"], costs = [1,10,100]
#
# 输出： -1
#
# 解释：
#
# 无法使 s 等于 target，因此返回 -1。
#
#
#
# 提示：
#
# 1 <= target.length <= 5 * 104
# 1 <= words.length == costs.length <= 5 * 104
# 1 <= words[i].length <= target.length
# 所有 words[i].length 的总和小于或等于 5 * 104
# target 和 words[i] 仅由小写英文字母组成。
# 1 <= costs[i] <= 104

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:

        n = len(target)
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

        m = max(len(w) for w in words)
        map = {}  # map: i -> dict  长度为i的字符串的字典，其中dict: hash -> cost  把一个哈希值映射到cost值

        for i, word in enumerate(words):
            # 依次计算每个word的哈希值
            v = 0
            for x in word:
                v = v * BASE + ord(x)
            if len(word) not in map:
                map[len(word)] = {v: costs[i]}
            else:
                map[len(word)][v] = costs[i]

        @cache
        def dfs(start):
            # 从位置start开始的子串，最小代价
            if start == n: return 0



so = Solution()
print(so.minimumCost(target = "abcdef", words = ["abdef","abc","d","def","ef"], costs = [100,1,1,10,5]))




