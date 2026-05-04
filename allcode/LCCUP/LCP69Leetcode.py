# 力扣嘉年华同样准备了纪念品展位，参观者只需要集齐 helloleetcode 的 13 张字母卡片即可获得力扣纪念章。
#
# 在展位上有一些由字母卡片拼成的单词，words[i][j] 表示第 i 个单词的第 j 个字母。
#
# 你可以从这些单词中取出一些卡片，但每次拿取卡片都需要消耗游戏代币，规则如下：
#
# 从一个单词中取一个字母所需要的代币数量，为该字母左边和右边字母数量之积
#
# 可以从一个单词中多次取字母，每个字母仅可被取一次
#
# 例如：从 example 中取出字母 a，需要消耗代币 2*4=8，字母取出后单词变为 exmple； 再从中取出字母 m，需要消耗代币 2*3=6，字母取出后单词变为 exple；
#
# 请返回取得 helloleetcode 这些字母需要消耗代币的 最少 数量。如果无法取得，返回 -1。
#
# 注意：
#
# 取出字母的顺序没有要求
# 取出的所有字母恰好可以拼成 helloleetcode
# 示例 1：
#
# 输入：words = ["hold","engineer","cost","level"]
#
# 输出：5
#
# 解释：最优方法为： 从 hold 依次取出 h、o、l、d， 代价均为 0 从 engineer 依次取出第 1 个 e 与最后一个 e， 代价为 0 和 5*1=5 从 cost 取出 c、o、t， 代价均为 0 从 level 依次取出 l、l、e、e， 代价均为 0 所有字母恰好可以拼成 helloleetcode，因此最小的代价为 5
#
# 示例 2：
#
# 输入：words = ["hello","leetcode"]
#
# 输出：0
#
# 提示：
#
# n == words.length
# m == words[i].length
# 1 <= n <= 24
# 1 <= m <= 8
# words[i][j] 仅为小写字母

from leetcode.allcode.competition.mypackage import *

class Solution:
    def Leetcode(self, words: List[str]) -> int:
        n = len(words)

        def xor(mask, sub):
            # 两个mask做异或操作，需要考虑 如：e 只允许出现 1000,1100,1110,1111
            res = (mask ^ sub) & 15
            co = (mask & (3 << 4)).bit_count() - (sub & (3 << 4)).bit_count()
            cl = (mask & (7 << 6)).bit_count() - (sub & (7 << 6)).bit_count()
            ce = (mask & (15 << 9)).bit_count() - (sub & (15 << 9)).bit_count()
            for i in range(co): res |= (1 << (5 - i))
            for i in range(cl): res |= (1 << (8 - i))
            for i in range(ce): res |= (1 << (12 - i))
            return res

        @cache
        def calc(word, mask):
            # word 在取mask对应的数时，最小的代价
            counter = Counter()
            if mask & 1: counter['h'] = 1
            if mask & (1 << 1): counter['c'] = 1
            if mask & (1 << 2): counter['d'] = 1
            if mask & (1 << 3): counter['t'] = 1
            counter['o'] = (mask & (3 << 4)).bit_count()
            counter['l'] = (mask & (7 << 6)).bit_count()
            counter['e'] = (mask & (15 << 9)).bit_count()
            m = len(word)
            cl = cr = 0  # 左右删掉的个数res

            def calc_p(l, r):
                # 左右双指针的方法，计算区间[l, r]需要的最小代价
                nonlocal cl, cr
                res1 = inf
                if l > r: return 0
                if l == r:
                    if counter[word[l]] == 0:
                        return 0
                    else:
                        return (l - cl) * (m - 1 - l - cr)
                if counter[word[l]] == 0 and counter[word[r]] == 0:
                    return calc_p(l + 1, r - 1)
                if counter[word[l]]:
                    counter[word[l]] -= 1
                    v = (l - cl) * (m - 1 - l - cr)
                    cl += 1
                    res1 = min(res1, v + calc_p(l + 1, r))
                    # 以下恢复现场
                    cl -= 1
                    counter[word[l]] += 1
                if counter[word[r]]:
                    counter[word[r]] -= 1
                    v = (r - cl) * (m - 1 - r - cr)
                    cr += 1
                    res1 = min(res1, v + calc_p(l, r - 1))
                    # 以下恢复现场
                    cr -= 1
                    counter[word[r]] += 1
                return res1
            return calc_p(0, m - 1)



        @cache
        def dfs(start, mask):
            # 从start个数开始，剩余需要选的字母为 mask时，需要的最小代价
            # mask的表示 4 bit 存 e剩余情况 只允许出现 1000,1100,1110,1111 4种，下面类似
            #           3 bit 存 l剩余情况
            #           2 bit 存 o剩余情况
            #           1 bit * 4 存 t/d/c/h剩余个数  0-1
            if start == n:
                return 0 if mask == 0 else inf
            ct = Counter(words[start])
            # mask 与 ct 取交集
            mask_r = 0  # 实际可取的所有mask
            if ct['h'] and mask & 1: mask_r = 1
            if ct['c'] and mask & (1 << 1): mask_r |= (1 << 1)
            if ct['d'] and mask & (1 << 2): mask_r |= (1 << 2)
            if ct['t'] and mask & (1 << 3): mask_r |= (1 << 3)
            cto = min(ct['o'], (mask & (3 << 4)).bit_count())
            for i in range(cto): mask_r |= (1 << (5 - i))
            ctl = min(ct['l'], (mask & (7 << 6)).bit_count())
            for i in range(ctl): mask_r |= (1 << (8 - i))
            cte = min(ct['e'], (mask & (15 << 9)).bit_count())
            for i in range(cte): mask_r |= (1 << (12 - i))
            sub = mask_r
            res = inf
            # 以下进行子集枚举
            while True:
                # 处理 sub 的逻辑
                # if start == 1:
                #     print(start, bin(sub))
                while True:
                    # 排除一些不合法的枚举
                    se = sub >> 9
                    if se not in {15, 14, 12, 8, 0}: break
                    sl = (sub & (7 << 6)) >> 6
                    if sl not in {7, 6, 4, 0}: break
                    so = (sub & (3 << 4)) >> 4
                    if so not in {3, 2, 0}: break

                    # 真正需要处理
                    # 计算 words[start] 取 sub时的最小操作代价
                    res1 = dfs(start + 1, xor(mask, sub))
                    res = min(res, res1 + calc(words[start], sub))
                    break
                sub = (sub - 1) & mask_r

                if sub == mask_r:
                    break
            return res

        ans = dfs(0, 31 << 9 | 7 << 6 | 3 << 4 | 15)
        return ans if ans < inf else -1



so = Solution()
print(so.Leetcode(words = ["l","col","he","col","odzetred","e"]))
print(so.Leetcode(words = ["hold","engineer","cost","level"]))




