# 我们正在玩一个猜数游戏，游戏规则如下：
#
# 我从1到 n 之间选择一个数字，你来猜我选了哪个数字。
#
# 每次你猜错了，我都会告诉你，我选的数字比你的大了或者小了。
#
# 然而，当你猜了数字 x 并且猜错了的时候，你需要支付金额为 x 的现金。直到你猜到我选的数字，你才算赢得了这个游戏。
#
# 示例:
#
# n = 10, 我选择了8.
#
# 第一轮: 你猜我选择的数字是5，我会告诉你，我的数字更大一些，然后你需要支付5块。
# 第二轮: 你猜是7，我告诉你，我的数字更大一些，你支付7块。
# 第三轮: 你猜是9，我告诉你，我的数字更小一些，你支付9块。
#
# 游戏结束。8 就是我选的数字。
#
# 你最终要支付 5 + 7 + 9 = 21 块钱。
# 给定n ≥ 1，计算你至少需要拥有多少现金才能确保你能赢得这个游戏。




from functools import lru_cache


class Solution:
    def getMoneyAmount(self, n: int) -> int:

        @lru_cache(None)
        def helper(start, end):  # 返回最小值和取到最小值时付了几次钱
            if end == start: return 0
            if start + 1 == end: return start

            ret = 100000
            for i in range(end - 1, (start + end) // 2 - 1, -1):
                value = i + max(helper(start, i - 1), helper(i + 1, end))
                ret = min(ret, value)
            # print(start, end, ret)
            return ret

        return helper(1, n)




so = Solution()
print(so.getMoneyAmount(7))
print(so.getMoneyAmount(4))
print(so.getMoneyAmount(10))

