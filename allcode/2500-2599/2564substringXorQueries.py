# 给你一个 二进制字符串 s 和一个整数数组 queries ，其中 queries[i] = [firsti, secondi] 。
#
# 对于第 i 个查询，找到 s 的 最短子字符串 ，它对应的 十进制值 val 与 firsti 按位异或 得到 secondi ，换言之，val ^ firsti == secondi 。
#
# 第 i 个查询的答案是子字符串 [lefti, righti] 的两个端点（下标从 0 开始），如果不存在这样的子字符串，则答案为 [-1, -1] 。如果有多个答案，请你选择 lefti 最小的一个。
#
# 请你返回一个数组 ans ，其中 ans[i] = [lefti, righti] 是第 i 个查询的答案。
#
# 子字符串 是一个字符串中一段连续非空的字符序列。
#
#
#
# 示例 1：
#
# 输入：s = "101101", queries = [[0,5],[1,2]]
# 输出：[[0,2],[2,3]]
# 解释：第一个查询，端点为 [0,2] 的子字符串为 "101" ，对应十进制数字 5 ，且 5 ^ 0 = 5 ，所以第一个查询的答案为 [0,2]。第二个查询中，端点为 [2,3] 的子字符串为 "11" ，对应十进制数字 3 ，且 3 ^ 1 = 2 。所以第二个查询的答案为 [2,3] 。
# 示例 2：
#
# 输入：s = "0101", queries = [[12,8]]
# 输出：[[-1,-1]]
# 解释：这个例子中，没有符合查询的答案，所以返回 [-1,-1] 。
# 示例 3：
#
# 输入：s = "1", queries = [[4,5]]
# 输出：[[0,0]]
# 解释：这个例子中，端点为 [0,0] 的子字符串对应的十进制值为 1 ，且 1 ^ 4 = 5 。所以答案为 [0,0] 。
#
#
# 提示：
#
# 1 <= s.length <= 104
# s[i] 要么是 '0' ，要么是 '1' 。
# 1 <= queries.length <= 105
# 0 <= firsti, secondi <= 109

from leetcode.allcode.competition.mypackage import *

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, idx, word: str) -> None:  # O(log(len(word)))
        cur = self.root
        for e in word:
            if e not in cur:
                cur[e] = {}
            cur = cur[e]
        if 'end' in cur:
            cur['end'].append(idx)
        else:
            cur['end'] = [idx]


    def search(self, word: str) -> list:
        cur = self.root
        ans = []
        for e in word:
            if e in cur:
                cur = cur[e]
                if 'end' in cur:
                    ans += cur['end']
            else:
                return ans
        return ans


class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        target = []
        for x, y in queries:
            target.append(bin(x ^ y)[2:])
        # print(target)
        tr = Trie()
        for i, t in enumerate(target):
            tr.insert(i, t)

        n = len(s)
        ans = [[-1, -1] for _ in range(len(queries))]
        for i in range(n):
            ids = tr.search(s[i:])
            if len(ids) == 0:
                continue
            for x in ids:
                if ans[x] != [-1, -1]:
                    continue
                ans[x] = [i, i + len(target[x]) - 1]
        return ans


        # ans = []
        # for t in target:
        #     pos = find(s, t)
        #     if pos == -1:
        #         ans.append([-1, -1])
        #     else:
        #         ans.append([pos, pos + len(t) - 1])
        # return ans



so = Solution()
print(so.substringXorQueries(s = "101101", queries = [[0,5],[1,2]]))
print(so.substringXorQueries(s = "0101", queries = [[12,8]]))
print(so.substringXorQueries(s = "1", queries = [[4,5]]))




