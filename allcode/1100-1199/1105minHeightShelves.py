# 给定一个数组 books ，其中 books[i] = [thicknessi, heighti] 表示第 i 本书的厚度和高度。你也会得到一个整数 shelfWidth 。
#
# 按顺序 将这些书摆放到总宽度为 shelfWidth 的书架上。
#
# 先选几本书放在书架上（它们的厚度之和小于等于书架的宽度 shelfWidth ），然后再建一层书架。重复这个过程，直到把所有的书都放在书架上。
#
# 需要注意的是，在上述过程的每个步骤中，摆放书的顺序与你整理好的顺序相同。
#
# 例如，如果这里有 5 本书，那么可能的一种摆放情况是：第一和第二本书放在第一层书架上，第三本书放在第二层书架上，第四和第五本书放在最后一层书架上。
# 每一层所摆放的书的最大高度就是这一层书架的层高，书架整体的高度为各层高之和。
#
# 以这种方式布置书架，返回书架整体可能的最小高度。
#
#
#
# 示例 1：
#
#
#
# 输入：books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4
# 输出：6
# 解释：
# 3 层书架的高度和为 1 + 3 + 2 = 6 。
# 第 2 本书不必放在第一层书架上。
# 示例 2:
#
# 输入: books = [[1,3],[2,4],[3,2]], shelfWidth = 6
# 输出: 4
#
#
# 提示：
#
# 1 <= books.length <= 1000
# 1 <= thicknessi <= shelfWidth <= 1000
# 1 <= heighti <= 1000

from leetcode.allcode.competition.mypackage import *
from functools import reduce, cache
from math import *


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        @cache
        def dfs(start):  # 第start本书，从一个新层开始，最少需要的高度
            if start >= n: return 0
            res = inf
            acc = 0  # 本层累积厚度
            mx_h = 0 # 本层最大高度
            while start < n:
                if acc + books[start][0] > shelfWidth:
                    break
                acc += books[start][0]
                mx_h = max(mx_h, books[start][1])
                res = min(res, mx_h + dfs(start + 1))
                start += 1
            # print(start, res)
            return res
        return dfs(0)



obj = Solution()
print(obj.minHeightShelves(books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4))
print(obj.minHeightShelves(books = [[1,3],[2,4],[3,2]], shelfWidth = 6))




