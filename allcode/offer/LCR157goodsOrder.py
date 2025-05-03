# 某店铺将用于组成套餐的商品记作字符串 goods，其中 goods[i] 表示对应商品。请返回该套餐内所含商品的 全部排列方式 。
#
# 返回结果 无顺序要求，但不能含有重复的元素。
#
#
#
# 示例 1：
#
# 输入：goods = "agew"
# 输出：["aegw","aewg","agew","agwe","aweg","awge","eagw","eawg","egaw","egwa","ewag","ewga","gaew","gawe","geaw","gewa","gwae","gwea","waeg","wage","weag","wega","wgae","wgea"]
#
#
# 提示：
#
# 1 <= goods.length <= 8

from leetcode.allcode.competition.mypackage import *

class Solution:
    def goodsOrder(self, goods: str) -> List[str]:
        n = len(goods)

        def dfs(vis):
            ans = set()
            if vis == (1 << n) - 1: return {''}
            for i in range(n):
                if vis & (1 << i) == 0:
                    res = dfs(vis | (1 << i))
                    for r in res:
                        ans.add(goods[i] + r)
            return ans

        return list(dfs(0))


so = Solution()
print(so.goodsOrder('agew'))




