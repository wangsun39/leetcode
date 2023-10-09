# 你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。
#
# 注意：本题中，每个活字字模只能使用一次。
#
#
#
# 示例 1：
#
# 输入："AAB"
# 输出：8
# 解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。
# 示例 2：
#
# 输入："AAABBC"
# 输出：188
# 示例 3：
#
# 输入："V"
# 输出：1
#
#
# 提示：
#
# 1 <= tiles.length <= 7
# tiles 由大写英文字母组成

from collections import Counter
from functools import cache
from typing import List


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = Counter(tiles)
        counter = counter.values()
        n = len(tiles)
        m = len(counter)
        # print(counter)

        @cache
        def dfs(idx, cnt):
            if idx == n: return 0 if sum(cnt) == n else 1
            res = 0
            for i, x in enumerate(cnt):
                if x > 0:
                    t = tuple(cnt[j] if j != i else cnt[j] - 1 for j in range(m))
                    res += dfs(idx + 1, t)
            if sum(cnt) == n:
                res += dfs(idx + 1, cnt)
            return res
        return dfs(0, tuple(counter))

so = Solution()
print(so.numTilePossibilities("AAB"))
print(so.numTilePossibilities("AAABBC"))

