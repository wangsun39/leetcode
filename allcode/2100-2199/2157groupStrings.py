# 给你一个下标从 0 开始的字符串数组 words 。每个字符串都只包含 小写英文字母 。words 中任意一个子串中，每个字母都至多只出现一次。
#
# 如果通过以下操作之一，我们可以从 s1 的字母集合得到 s2 的字母集合，那么我们称这两个字符串为 关联的 ：
#
# 往 s1 的字母集合中添加一个字母。
# 从 s1 的字母集合中删去一个字母。
# 将 s1 中的一个字母替换成另外任意一个字母（也可以替换为这个字母本身）。
# 数组 words 可以分为一个或者多个无交集的 组 。如果一个字符串与另一个字符串关联，那么它们应当属于同一个组。
#
# 注意，你需要确保分好组后，一个组内的任一字符串与其他组的字符串都不关联。可以证明在这个条件下，分组方案是唯一的。
#
# 请你返回一个长度为 2 的数组 ans ：
#
# ans[0] 是 words 分组后的 总组数 。
# ans[1] 是字符串数目最多的组所包含的字符串数目。
#
#
# 示例 1：
#
# 输入：words = ["a","b","ab","cde"]
# 输出：[2,3]
# 解释：
# - words[0] 可以得到 words[1] （将 'a' 替换为 'b'）和 words[2] （添加 'b'）。所以 words[0] 与 words[1] 和 words[2] 关联。
# - words[1] 可以得到 words[0] （将 'b' 替换为 'a'）和 words[2] （添加 'a'）。所以 words[1] 与 words[0] 和 words[2] 关联。
# - words[2] 可以得到 words[0] （删去 'b'）和 words[1] （删去 'a'）。所以 words[2] 与 words[0] 和 words[1] 关联。
# - words[3] 与 words 中其他字符串都不关联。
# 所以，words 可以分成 2 个组 ["a","b","ab"] 和 ["cde"] 。最大的组大小为 3 。
# 示例 2：
#
# 输入：words = ["a","ab","abc"]
# 输出：[1,3]
# 解释：
# - words[0] 与 words[1] 关联。
# - words[1] 与 words[0] 和 words[2] 关联。
# - words[2] 与 words[1] 关联。
# 由于所有字符串与其他字符串都关联，所以它们全部在同一个组内。
# 所以最大的组大小为 3 。
#
#
# 提示：
#
# 1 <= words.length <= 2 * 104
# 1 <= words[i].length <= 26
# words[i] 只包含小写英文字母。
# words[i] 中每个字母最多只出现一次。

from leetcode.allcode.competition.mypackage import *

class UnionFind:
    def __init__(self, n: int):
        # 一开始有 n 个集合 {0}, {1}, ..., {n-1}
        # 集合 i 的代表元是自己
        self._fa = list(range(n))  # 代表元
        self.cc = n  # 连通块个数

    # 返回 x 所在集合的代表元
    # 同时做路径压缩，也就是把 x 所在集合中的所有元素的 fa 都改成代表元
    def find(self, x: int) -> int:
        # 如果 fa[x] == x，则表示 x 是代表元
        if self._fa[x] != x:
            self._fa[x] = self.find(self._fa[x])  # fa 改成代表元
        return self._fa[x]

    # 把 from 所在集合合并到 to 所在集合中
    # 返回是否合并成功
    def merge(self, from_: int, to: int) -> bool:
        x, y = self.find(from_), self.find(to)
        if x == y:  # from 和 to 在同一个集合，不做合并
            return False
        self._fa[x] = y  # 合并集合。修改后就可以认为 from 和 to 在同一个集合了
        self.cc -= 1  # 成功合并，连通块个数减一
        return True

    def get_max_group(self):
        counter = Counter(self._fa)
        return max(counter.values())

class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        n = len(words)
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        uf = UnionFind(n)
        idx = {}  # 精确匹配
        idx2 = {}  # 模糊匹配，用于替换匹配，第27位是个通配
        for i, w in enumerate(words):
            c = 0
            for x in w:
                c |= (1 << c2i[x])
            s = {c}
            if c in idx:
                uf.merge(idx[c], i)
            else:
                idx[c] = i
            c1 = [k for k in range(26) if (c & (1 << k)) > 0]
            c2 = [k for k in range(26) if (c & (1 << k)) == 0]
            # 加一个字母
            for j in c2:
                c ^= (1 << j)
                s.add(c)
                c ^= (1 << j)
            # 减一个字母
            for j in c1:
                c ^= (1 << j)
                s.add(c)
                c ^= (1 << j)
            # 改一个字母
            c ^= (1 << 26)
            for j in c1:
                c ^= (1 << j)
                if c in idx2:
                    uf.merge(idx2[c], i)
                else:
                    idx2[c] = i
                c ^= (1 << j)
            c ^= (1 << 26)
            for ss in s:
                if ss in idx and idx[ss] != i:
                    uf.merge(idx[ss], i)
        for i in range(n):
            uf.find(i)
        ans = [0, 0]
        ans[0] = uf.cc
        ans[1] = uf.get_max_group()
        return ans





so = Solution()
print(so.groupStrings(words = ["a","b","ab","cde"]))
print(so.groupStrings(words = ["qamp","am","khdrn"]))




