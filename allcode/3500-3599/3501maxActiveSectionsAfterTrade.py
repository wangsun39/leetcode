# 给你一个长度为 n 的二进制字符串 s ，其中：
#
# '1' 表示一个 活跃 区段。
# '0' 表示一个 非活跃 区段。
# 你最多可以进行一次 操作 来最大化 s 中活跃区段的数量。在一次操作中，你可以：
#
# 将一个被 '0' 包围的连续 '1' 区块转换为全 '0'。
# 然后，将一个被 '1' 包围的连续 '0' 区块转换为全 '1'。
# 此外，你还有一个 二维数组 queries，其中 queries[i] = [li, ri] 表示子字符串 s[li...ri]。
#
# 对于每个查询，确定在对子字符串 s[li...ri] 进行最优交换后，字符串 s 中 可能的最大 活跃区段数。
#
# 返回一个数组 answer，其中 answer[i] 是 queries[i] 的结果。
#
# 注意
#
# 对于每个查询，仅对 s[li...ri] 处理时，将其看作是在两端都加上一个 '1' 后的字符串，形成 t = '1' + s[li...ri] + '1'。这些额外的 '1' 不会对最终的活跃区段数有贡献。
# 各个查询相互独立。
#
#
# 示例 1：
#
# 输入： s = "01", queries = [[0,1]]
#
# 输出： [1]
#
# 解释：
#
# 因为没有被 '0' 包围的 '1' 区块，所以没有有效的操作可以进行。最大活跃区段数是 1。
#
# 示例 2：
#
# 输入： s = "0100", queries = [[0,3],[0,2],[1,3],[2,3]]
#
# 输出： [4,3,1,1]
#
# 解释：
#
# 查询 [0, 3] → 子字符串 "0100" → 变为 "101001"
# 选择 "0100"，"0100" → "0000" → "1111"。
# 最终字符串（去掉添加的 '1'）为 "1111"。最大活跃区段数为 4。
#
# 查询 [0, 2] → 子字符串 "010" → 变为 "10101"
# 选择 "010"，"010" → "000" → "111"。
# 最终字符串（去掉添加的 '1'）为 "1110"。最大活跃区段数为 3。
#
# 查询 [1, 3] → 子字符串 "100" → 变为 "11001"
# 因为没有被 '0' 包围的 '1' 区块，所以没有有效的操作可以进行。最大活跃区段数为 1。
#
# 查询 [2, 3] → 子字符串 "00" → 变为 "1001"
# 因为没有被 '0' 包围的 '1' 区块，所以没有有效的操作可以进行。最大活跃区段数为 1。
#
# 示例 3：
#
# 输入： s = "1000100", queries = [[1,5],[0,6],[0,4]]
#
# 输出： [6,7,2]
#
# 解释：
#
# 查询 [1, 5] → 子字符串 "00010" → 变为 "1000101"
# 选择 "00010"，"00010" → "00000" → "11111"。
# 最终字符串（去掉添加的 '1'）为 "1111110"。最大活跃区段数为 6。
#
# 查询 [0, 6] → 子字符串 "1000100" → 变为 "110001001"
# 选择 "000100"，"000100" → "000000" → "111111"。
# 最终字符串（去掉添加的 '1'）为 "1111111"。最大活跃区段数为 7。
#
# 查询 [0, 4] → 子字符串 "10001" → 变为 "1100011"
# 因为没有被 '0' 包围的 '1' 区块，所以没有有效的操作可以进行。最大活跃区段数为 2。
#
# 示例 4：
#
# 输入： s = "01010", queries = [[0,3],[1,4],[1,3]]
#
# 输出： [4,4,2]
#
# 解释：
#
# 查询 [0, 3] → 子字符串 "0101" → 变为 "101011"
# 选择 "010"，"010" → "000" → "111"。
# 最终字符串（去掉添加的 '1'）为 "11110"。最大活跃区段数为 4。
#
# 查询 [1, 4] → 子字符串 "1010" → 变为 "110101"
# 选择 "010"，"010" → "000" → "111"。
# 最终字符串（去掉添加的 '1'）为 "01111"。最大活跃区段数为 4。
#
# 查询 [1, 3] → 子字符串 "101" → 变为 "11011"
# 因为没有被 '0' 包围的 '1' 区块，所以没有有效的操作可以进行。最大活跃区段数为 2。
#
#
#
# 提示：
#
# 1 <= n == s.length <= 105
# 1 <= queries.length <= 105
# s[i] 只有 '0' 或 '1'。
# queries[i] = [li, ri]
# 0 <= li <= ri < n

from leetcode.allcode.competition.mypackage import *

class SparseTable:
    def __init__(self, arr: list, func=max):
        self.func = func
        self.n = len(arr)
        self.log = [0] * (self.n + 1)

        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1

        self.k = self.log[self.n]
        self.st = [[0] * (self.n) for _ in range(self.k + 1)]
        self.st[0] = arr

        for j in range(1, self.k + 1):
            i = 0
            while i + (1 << j) <= self.n:
                self.st[j][i] = self.func(
                    self.st[j - 1][i], self.st[j - 1][i + (1 << (j - 1))]
                )
                i += 1

    def query(self, left: int, right: int):  # 闭区间查询
        j = self.log[right - left + 1]
        return self.func(self.st[j][left], self.st[j][right - (1 << j) + 1])


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        c1 = s.count('1')
        start0 = -1
        seg0 = []  # 记录每个0的段的长度
        l0 = []  # 记录每个0的段的左端点
        r0 = []  # 记录每个0的段的右端点
        # r0[i]-lp[i]+1==seg0[i]
        for i, x in enumerate(s):
            if x == '0':
                if start0 == -1:
                    start0 = i
                    l0.append(i)
                    r0.append(i)
                    seg0.append(1)
                else:
                    r0[-1] = i
                    seg0[-1] += 1
            else:
                start0 = -1
        # print(l0)
        # print(r0)
        # print(seg0)
        # 计算seg0的相邻和
        pair_seg0 = []
        pair_l0 = []
        pair_r0 = []
        for i in range(len(seg0) - 1):
            pair_seg0.append(seg0[i] + seg0[i + 1])
            pair_l0.append(l0[i])
            pair_r0.append(r0[i + 1])
        # print(pair_l0)
        # print(pair_r0)
        # print(pair_seg0)

        if len(pair_l0) == 0:
            return [c1] * len(queries)

        st = SparseTable(pair_seg0)  # 相邻和放入 ST 表
        ans = []
        for l, r in queries:
            # 根据l,r确定st表中的sl和sr，闭区间 [sl, sr]
            sl = bisect_left(pair_l0, l)
            sr = bisect_right(pair_r0, r) - 1
            if sl <= sr:  # 至少包含一个完整的 pair_seg0 段，即至少包含两个完整的 seg0 段
                v = st.query(sl, sr)
            else:
                v = 0

            if s[l] == '1' == s[r]:
                ans.append(c1 + v)
                continue

            p1 = bisect_right(l0, l) - 1
            p2 = bisect_right(l0, r) - 1
            if p1 == p2:
                # [l,r] 中至多包含一段完整seg0
                ans.append(c1 + v)
                continue
            if p1 + 1 == p2:
                if sl <= sr:
                    ans.append(c1 + v)  # 恰好包含2个完整的 seg0 段
                    continue
                if s[l] == '1':  # 仅包含至多1个完整的 seg0 段
                    ans.append(c1)
                    continue
                # 相邻的两个段的一部分可以拼出更多的1
                v = 0
                if s[l] == '0':
                    v += r0[p1] - l + 1
                if s[r] == '0':
                    v += r - l0[p2] + 1
                else: # 包含完整的第二个 seg0 段
                    v += seg0[p2]
                ans.append(c1 + v)
                continue
            # 首尾两个部分 seg0 段，是否能拼成出比st表中更长的段
            if s[l] == '0':
                v = max(v, r0[p1] - l + 1 + seg0[p1 + 1])
            if s[r] == '0':
                v = max(v, r - l0[p2] + 1 + seg0[p2 - 1])
            ans.append(c1 + v)
        return ans





so = Solution()
print(so.maxActiveSectionsAfterTrade(s = "0101110001101", queries = [[0,12]]))
print(so.maxActiveSectionsAfterTrade(s = "1100110011", queries = [[3,9],[0,7],[4,9],[1,9]]))
print(so.maxActiveSectionsAfterTrade(s = "0100", queries = [[0,3],[0,2],[1,3],[2,3]]))




