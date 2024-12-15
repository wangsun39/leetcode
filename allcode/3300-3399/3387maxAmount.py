# 给你一个字符串 initialCurrency，表示初始货币类型，并且你一开始拥有 1.0 单位的 initialCurrency。
#
# 另给你四个数组，分别表示货币对（字符串）和汇率（实数）：
#
# pairs1[i] = [startCurrencyi, targetCurrencyi] 表示在 第 1 天，可以按照汇率 rates1[i] 将 startCurrencyi 转换为 targetCurrencyi。
# pairs2[i] = [startCurrencyi, targetCurrencyi] 表示在 第 2 天，可以按照汇率 rates2[i] 将 startCurrencyi 转换为 targetCurrencyi。
# 此外，每种 targetCurrency 都可以以汇率 1 / rate 转换回对应的 startCurrency。
# 你可以在 第 1 天 使用 rates1 进行任意次数的兑换（包括 0 次），然后在 第 2 天 使用 rates2 再进行任意次数的兑换（包括 0 次）。
#
# 返回在两天兑换后，最大可能拥有的 initialCurrency 的数量。
#
# 注意：汇率是有效的，并且第 1 天和第 2 天的汇率之间相互独立，不会产生矛盾。
#
#
#
# 示例 1：
#
# 输入： initialCurrency = "EUR", pairs1 = [["EUR","USD"],["USD","JPY"]], rates1 = [2.0,3.0], pairs2 = [["JPY","USD"],["USD","CHF"],["CHF","EUR"]], rates2 = [4.0,5.0,6.0]
#
# 输出： 720.00000
#
# 解释：
#
# 根据题目要求，需要最大化最终的 EUR 数量，从 1.0 EUR 开始：
#
# 第 1 天：
# 将 EUR 换成 USD，得到 2.0 USD。
# 将 USD 换成 JPY，得到 6.0 JPY。
# 第 2 天：
# 将 JPY 换成 USD，得到 24.0 USD。
# 将 USD 换成 CHF，得到 120.0 CHF。
# 最后将 CHF 换回 EUR，得到 720.0 EUR。
# 示例 2：
#
# 输入： initialCurrency = "NGN", pairs1 = [["NGN","EUR"]], rates1 = [9.0], pairs2 = [["NGN","EUR"]], rates2 = [6.0]
#
# 输出： 1.50000
#
# 解释：
#
# 在第 1 天将 NGN 换成 EUR，并在第 2 天用反向汇率将 EUR 换回 NGN，可以最大化最终的 NGN 数量。
#
# 示例 3：
#
# 输入： initialCurrency = "USD", pairs1 = [["USD","EUR"]], rates1 = [1.0], pairs2 = [["EUR","JPY"]], rates2 = [10.0]
#
# 输出： 1.00000
#
# 解释：
#
# 在这个例子中，不需要在任何一天进行任何兑换。
#
#
#
# 提示：
#
# 1 <= initialCurrency.length <= 3
# initialCurrency 仅由大写英文字母组成。
# 1 <= n == pairs1.length <= 10
# 1 <= m == pairs2.length <= 10
# pairs1[i] == [startCurrencyi, targetCurrencyi]
# pairs2[i] == [startCurrencyi, targetCurrencyi]
# 1 <= startCurrencyi.length, targetCurrencyi.length <= 3
# startCurrencyi 和 targetCurrencyi 仅由大写英文字母组成。
# rates1.length == n
# rates2.length == m
# 1.0 <= rates1[i], rates2[i] <= 10.0
# 输入保证两个转换图在各自的天数中没有矛盾或循环。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        country = set()
        for p in pairs1 + pairs2:
            for pp in p:
                country.add(pp)

        n1, n2 = len(pairs1), len(pairs2)
        g1 = defaultdict(list)
        for i in range(n1):
            c1, c2 = pairs1[i]
            ra = rates1[i]
            g1[c1].append([c2, ra])
            g1[c2].append([c1, 1.0 / ra])

        g2 = defaultdict(list)
        for i in range(n2):
            c1, c2 = pairs2[i]
            ra = rates2[i]
            g2[c1].append([c2, ra])
            g2[c2].append([c1, 1.0 / ra])

        def dijkstra(g, start, init_val):   # 从start开始的最长路径
            dist = defaultdict(float)  # 注意这个地方可能要替换成 n
            dist[start] = init_val
            h = [(-init_val, start)]
            while h:
                d, x = heappop(h)
                if -d < dist[x]:
                    continue
                for y, wt in g[x]:
                    new_d = dist[x] * wt
                    if new_d > dist[y]:
                        dist[y] = new_d
                        heappush(h, (-new_d, y))
            return dist

        s1 = dijkstra(g1, initialCurrency, 1.0)

        ans = 0
        for co in country:
            v1 = s1[co]
            s2 = dijkstra(g2, co, v1)
            if ans < s2[initialCurrency]:
                ans = s2[initialCurrency]

        return ans




so = Solution()
print(so.maxAmount(initialCurrency = "EUR", pairs1 = [["EUR","USD"],["USD","JPY"]], rates1 = [2.0,3.0], pairs2 = [["JPY","USD"],["USD","CHF"],["CHF","EUR"]], rates2 = [4.0,5.0,6.0]))
print(so.maxAmount(initialCurrency = "NGN", pairs1 = [["NGN","EUR"]], rates1 = [9.0], pairs2 = [["NGN","EUR"]], rates2 = [6.0]))
print(so.maxAmount(initialCurrency = "USD", pairs1 = [["USD","EUR"]], rates1 = [1.0], pairs2 = [["EUR","JPY"]], rates2 = [10.0]))




