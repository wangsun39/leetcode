# 「力扣挑战赛」心算项目的挑战比赛中，要求选手从 N 张卡牌中选出 cnt 张卡牌，若这 cnt 张卡牌数字总和为偶数，则选手成绩「有效」且得分为 cnt 张卡牌数字总和。
# 给定数组 cards 和 cnt，其中 cards[i] 表示第 i 张卡牌上的数字。 请帮参赛选手计算最大的有效得分。若不存在获取有效得分的卡牌方案，则返回 0。
#
# 示例 1：
#
# 输入：cards = [1,2,8,9], cnt = 3
#
# 输出：18
#
# 解释：选择数字为 1、8、9 的这三张卡牌，此时可获得最大的有效得分 1+8+9=18。
#
# 示例 2：
#
# 输入：cards = [3,3,1], cnt = 1
#
# 输出：0
#
# 解释：不存在获取有效得分的卡牌方案。
#
# 提示：
#
# 1 <= cnt <= cards.length <= 10^5
# 1 <= cards[i] <= 1000
#
# https://leetcode.cn/problems/uOAnQW



from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort()
        n = len(cards)
        s = sum(cards[n - cnt:])
        if s & 1 == 0:
            return s

        odd, even = -1, -1
        for i in range(n - cnt, n):
            if i != -1 and cards[i] & 1 == 0 and even == -1:
                even = i
            elif i != -1 and cards[i] & 1 == 1 and odd == -1:
                odd = i
        s1, s2 = 0, 0
        for i in range(n - cnt - 1, -1, -1):
            if cards[i] & 1 == 0 and odd != -1 and s1 == 0:
                s1 = s - cards[odd] + cards[i]
            elif cards[i] & 1 == 1 and even != -1 and s2 == 0:
                s2 = s - cards[even] + cards[i]
            if s1 and s2:
                return max(s1, s2)
        return max(s1, s2)


so = Solution()
print(so.maxmiumScore(cards = [7,6,4,6], cnt = 1))
print(so.maxmiumScore(cards = [3,1,6,9,2,4,9,2,3], cnt = 4))
print(so.maxmiumScore(cards = [1,2,8,9], cnt = 3))
print(so.maxmiumScore(cards = [3,3,1], cnt = 1))




