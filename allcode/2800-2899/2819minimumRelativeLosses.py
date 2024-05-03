# 现给定一个整数数组 prices，表示巧克力的价格；以及一个二维整数数组 queries，其中 queries[i] = [ki, mi]。
#
# Alice 和 Bob 去买巧克力，Alice 提出了一种付款方式，而 Bob 同意了。
#
# 对于每个 queries[i] ，它的条件如下：
#
# 如果一块巧克力的价格 小于等于 ki，那么 Bob 为它付款。
# 否则，Bob 为其中 ki 部分付款，而 Alice 为 剩余 部分付款。
# Bob 想要选择 恰好 mi 块巧克力，使得他的 相对损失最小 。更具体地说，如果总共 Alice 付款了 ai，Bob 付款了 bi，那么 Bob 希望最小化 bi - ai。
#
# 返回一个整数数组 ans，其中 ans[i] 是 Bob 在 queries[i] 中可能的 最小相对损失 。
#
#
#
# 示例 1：
#
# 输入：prices = [1,9,22,10,19], queries = [[18,4],[5,2]]
# 输出：[34,-21]
# 解释：对于第一个 query，Bob 选择价格为 [1,9,10,22] 的巧克力。他付了 1 + 9 + 10 + 18 = 38，Alice 付了 0 + 0 + 0 + 4 = 4。因此，Bob 的相对损失是 38 - 4 = 34。
# 对于第二个 query，Bob 选择价格为 [19,22] 的巧克力。他付了 5 + 5 = 10，Alice 付了 14 + 17 = 31。因此，Bob 的相对损失是 10 - 31 = -21。
# 可以证明这些是可能的最小相对损失。
# 示例 2：
#
# 输入：prices = [1,5,4,3,7,11,9], queries = [[5,4],[5,7],[7,3],[4,5]]
# 输出：[4,16,7,1]
# 解释：对于第一个 query，Bob 选择价格为 [1,3,9,11] 的巧克力。他付了 1 + 3 + 5 + 5 = 14，Alice 付了 0 + 0 + 4 + 6 = 10。因此，Bob 的相对损失是 14 - 10 = 4。
# 对于第二个 query，Bob 必须选择所有的巧克力。他付了 1 + 5 + 4 + 3 + 5 + 5 + 5 = 28，Alice 付了 0 + 0 + 0 + 0 + 2 + 6 + 4 = 12。因此，Bob 的相对损失是 28 - 12 = 16。
# 对于第三个 query，Bob 选择价格为 [1,3,11] 的巧克力。他付了 1 + 3 + 7 = 11，Alice 付了 0 + 0 + 4 = 4。因此，Bob 的相对损失是 11 - 4 = 7。
# 对于第四个 query，Bob 选择价格为 [1,3,7,9,11] 的巧克力。他付了 1 + 3 + 4 + 4 + 4 = 16，Alice 付了 0 + 0 + 3 + 5 + 7 = 15。因此，Bob 的相对损失是 16 - 15 = 1。
# 可以证明这些是可能的最小相对损失。
# 示例 3：
#
# 输入：prices = [5,6,7], queries = [[10,1],[5,3],[3,3]]
# 输出：[5,12,0]
# 解释：对于第一个 query，Bob 选择价格为 5 的巧克力。他付了 5，Alice 付了 0。因此，Bob 的相对损失是 5 - 0 = 5。
# 对于第二个 query，Bob 必须选择所有的巧克力。他付了 5 + 5 + 5 = 15，Alice 付了 0 + 1 + 2 = 3。因此，Bob 的相对损失是 15 - 3 = 12。
# 对于第三个 query，Bob 必须选择所有的巧克力。他付了 3 + 3 + 3 = 9，Alice 付了 2 + 3 + 4 = 9。因此，Bob 的相对损失是 9 - 9 = 0。
# 可以证明这些是可能的最小相对损失。
#
#
# 提示：
#
# 1 <= prices.length == n <= 105
# 1 <= prices[i] <= 109
# 1 <= queries.length <= 105
# queries[i].length == 2
# 1 <= ki <= 109
# 1 <= mi <= n

from leetcode.allcode.competition.mypackage import *


class Solution:
    def minimumRelativeLosses(self, prices: List[int], queries: List[List[int]]) -> List[int]:
        prices.sort()
        s = list(accumulate(prices, initial=0))
        ans = []
        for k, m in queries:
            n1 = bisect_right(prices, k)
            n2 = max(m - n1, 0)
            sum_bob = s[n1] + n2 * k
            ans.append(sum_bob * 2 - s[m])
        return ans




so = Solution()
print(so.minimumRelativeLosses(prices = [1,9,22,10,19], queries = [[18,4],[5,2]]))




