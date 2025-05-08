# 购物车内的商品价格按照升序记录于数组 price。请在购物车中找到两个商品的价格总和刚好是 target。若存在多种情况，返回任一结果即可。
#
# 示例 1：
#
# 输入：price = [3, 9, 12, 15], target = 18
# 输出：[3,15] 或者 [15,3]
# 示例 2：
#
# 输入：price = [8, 21, 27, 34, 52, 66], target = 61
# 输出：[27,34] 或者 [34,27]
#
#
# 提示：
#
# 1 <= price.length <= 10^5
# 1 <= price[i] <= 10^6
# 1 <= target <= 2*10^6

from leetcode.allcode.competition.mypackage import *

class Solution:
    def twoSum(self, price: List[int], target: int) -> List[int]:
        n = len(price)
        j = n - 1
        for i in range(n):
            while price[i] + price[j] > target:
                j -= 1

            if price[i] + price[j] == target:
                return [price[i], price[j]]




so = Solution()
print(so.twoSum(price = [3, 9, 12, 15], target = 18))




