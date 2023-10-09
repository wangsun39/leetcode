# 给你两个整数 n 和 k ，请你构造一个答案列表 answer ，该列表应当包含从 1 到 n 的 n 个不同正整数，并同时满足下述条件：
#
# 假设该列表是 answer = [a1, a2, a3, ... , an] ，那么列表 [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] 中应该有且仅有 k 个不同整数。
# 返回列表 answer 。如果存在多种答案，只需返回其中 任意一种 。
#
#  
#
# 示例 1：
#
# 输入：n = 3, k = 1
# 输出：[1, 2, 3]
# 解释：[1, 2, 3] 包含 3 个范围在 1-3 的不同整数，并且 [1, 1] 中有且仅有 1 个不同整数：1
# 示例 2：
#
# 输入：n = 3, k = 2
# 输出：[1, 3, 2]
# 解释：[1, 3, 2] 包含 3 个范围在 1-3 的不同整数，并且 [2, 1] 中有且仅有 2 个不同整数：1 和 2
#  
#
# 提示：
#
# 1 <= k < n <= 104

from typing import List
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        def construct(k):
            half = (k + 1) // 2
            ans = [0] * k
            for i in range(half):
                ans[i * 2] = i + 1
                if i * 2 + 1 < k:
                    ans[i * 2 + 1] = k - i
            return ans
        ans = construct(k + 1)
        for i in range(k + 2, n + 1):
            ans.append(i)
        return ans


so = Solution()
print(so.constructArray(n = 3, k = 1))
print(so.constructArray(n = 3, k = 2))
print(so.constructArray(n = 5, k = 2))

