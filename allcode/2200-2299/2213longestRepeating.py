# 给你一个下标从 0 开始的字符串 s 。另给你一个下标从 0 开始、长度为 k 的字符串 queryCharacters ，一个下标从 0 开始、长度也是 k 的整数 下标 数组 queryIndices ，这两个都用来描述 k 个查询。
#
# 第 i 个查询会将 s 中位于下标 queryIndices[i] 的字符更新为 queryCharacters[i] 。
#
# 返回一个长度为 k 的数组 lengths ，其中 lengths[i] 是在执行第 i 个查询 之后 s 中仅由 单个字符重复 组成的 最长子字符串 的 长度 。
#
#
#
# 示例 1：
#
# 输入：s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
# 输出：[3,3,4]
# 解释：
# - 第 1 次查询更新后 s = "bbbacc" 。由单个字符重复组成的最长子字符串是 "bbb" ，长度为 3 。
# - 第 2 次查询更新后 s = "bbbccc" 。由单个字符重复组成的最长子字符串是 "bbb" 或 "ccc"，长度为 3 。
# - 第 3 次查询更新后 s = "bbbbcc" 。由单个字符重复组成的最长子字符串是 "bbbb" ，长度为 4 。
# 因此，返回 [3,3,4] 。
# 示例 2：
#
# 输入：s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
# 输出：[2,3]
# 解释：
# - 第 1 次查询更新后 s = "abazz" 。由单个字符重复组成的最长子字符串是 "zz" ，长度为 2 。
# - 第 2 次查询更新后 s = "aaazz" 。由单个字符重复组成的最长子字符串是 "aaa" ，长度为 3 。
# 因此，返回 [2,3] 。
#
#
# 提示：
#
# 1 <= s.length <= 105
# s 由小写英文字母组成
# k == queryCharacters.length == queryIndices.length
# 1 <= k <= 105
# queryCharacters 由小写英文字母组成
# 0 <= queryIndices[i] < s.length

from leetcode.allcode.competition.mypackage import *

class STree2:
    # 非动态开点，单点更新，区间查询
    def __init__(self, s: list):
        # self.n = n
        n = len(s)
        self.s = s
        self.max = [1] * (2 << n.bit_length())  # 对应区间的最大连续子串长度
        self.pre = [1] * (2 << n.bit_length())  # 对应区间的前缀最大连续子串长度
        self.suff = [1] * (2 << n.bit_length())  # 对应区间的后缀最大连续子串长度


    # 线段树：把下标 i 上的元素值增加 val，单点更新
    # o 是当前区间对应的下标，[l, r]当前区间的范围
    # 更新包含下标i的所有区间
    def update(self, o: int, l: int, r: int, i: int) -> None:
        if l == r:
            return
        m = (l + r) // 2
        if i <= m:
            self.update(o * 2, l, m, i)
        else:
            self.update(o * 2 + 1, m + 1, r, i)
        if self.s[m] == self.s[m + 1]:
            if self.pre[o * 2] == m - l + 1:
                self.pre[o] = self.pre[o * 2] + self.pre[o * 2 + 1]
            else:
                self.pre[o] = self.pre[o * 2]
            if self.suff[o * 2 + 1] == r - m:
                self.suff[o] = self.suff[o * 2] + self.suff[o * 2 + 1]
            else:
                self.suff[o] = self.suff[o * 2 + 1]
            self.max[o] = max(self.max[o * 2], self.max[o * 2 + 1], self.suff[o * 2] + self.pre[o * 2 + 1])
        else:
            self.max[o] = max(self.max[o * 2], self.max[o * 2 + 1])
            self.pre[o] = self.pre[o * 2]
            self.suff[o] = self.suff[o * 2 + 1]

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        ans = []
        n = len(s)
        sn = list(range(n))
        st = STree2(sn)   # 为了对应线段树成员 max/pre/suff 都是1的初始值，构造一个初始的sn，这样只需用一个update函数就可以了
        for i in range(n):
            st.s[i] = s[i]
            st.update(1, 0, n - 1, i)
        for i, x in zip(queryIndices, queryCharacters):
            st.s[i] = x
            st.update(1, 0, n - 1, i)
            ans.append(st.max[1])
        return ans




so = Solution()
print(so.longestRepeating(s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]))
print(so.longestRepeating(s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]))




